import json

import pytest
from py.xml import html
from config import RunConfig
import allure
from slugify import slugify
from common.config import *
from playwright.sync_api import sync_playwright, expect
from page.login_page import LoginPage


# 定义基本测试环境
@pytest.fixture(scope='session')
def base_url():
    return RunConfig.baseUrl


@pytest.fixture(scope='session')
def baseUrl_baidu():
    return RunConfig.baseUrl_baidu


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
    allure报告模版
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    """
    if call.when == "call":
        # 失败的情况下
        if call.excinfo is not None and "page" in item.funcargs:
            from playwright.async_api import Page
            page: Page = item.funcargs["page"]

            allure.attach(
                page.screenshot(type='png'),
                name=f"{slugify(item.nodeid)}.png",
                attachment_type=allure.attachment_type.PNG
            )

            # # 向报告中添加视频
            # video_path = page.video.path()
            # page.context.close()  # ensure video saved
            # allure.attach(
            #     open(video_path, 'rb').read(),
            #     name=f"{slugify(item.nodeid)}.webm",
            #     attachment_type=allure.attachment_type.WEBM
            # )

    callers = yield


def capture_screenshots(case_name, page):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    if RunConfig.NEW_REPORT is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.NEW_REPORT, "image", file_name)
        page.screenshot(path=image_dir)


#     context.close()

@pytest.fixture(scope="session")
def login_page():
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False)
        permissions = ["clipboard-read", "clipboard-write"]
        context1 = browser.new_context(permissions=permissions)
        # 录制日志
        context1.tracing.start(screenshots=True, snapshots=True, sources=True)
        login_page = context1.new_page()
        yield login_page
        # 保存登录状态
        storage = context1.storage_state()
        with open("state.json", "w") as f:
            f.write(json.dumps(storage))
        # 保存日志
        context1.tracing.stop(path="trace.zip")
        context1.close()
        browser.close()


@pytest.fixture(scope="class")
def page(base_url):
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False)
        permissions = ["clipboard-read", "clipboard-write"]
        context = browser.new_context(permissions=permissions)
        # 录制日志
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto(base_url)
        page.locator(LoginPage.login_but).click()
        page.locator(LoginPage.phone_num).fill("15557993309")
        page.locator(LoginPage.send_sms_but).click()
        page.locator(LoginPage.input_sms).fill("888888")
        # 有时登录频繁需要滑动验证码

        dropbutton = page.locator(LoginPage.veriy)
        print(dropbutton.all())
        if page.is_visible(LoginPage.veriy):
            # 获取拖动按钮位置并拖动
            box = dropbutton.bounding_box()

            page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2)

            page.mouse.down()

            mov_x = box['x'] + box['width'] / 2 + 260

            page.mouse.move(mov_x, box['y'] + box['height'] / 2)

            page.mouse.up()
            print(dropbutton.all())
        else:
            pass
        page.locator(LoginPage.commit_but).click()
        yield page
        # 保存日志
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()


@pytest.fixture(scope="class")
def logged_page(base_url):
    ss_file = '/Users/mac/Downloads/playwright-demo/auth/state.json'
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False)
        permissions = ["clipboard-read", "clipboard-write"]
        # 判断是否存在状态文件，有的话就加载
        if os.path.isfile(ss_file):
            context = browser.new_context(storage_state=ss_file, permissions=permissions)
            # print("登录文件存在，使用已登录状态")
        else:
            context = browser.new_context()
            # print("登录文件不存在，重新登录登录状态")
        logged_page = context.new_page()
        # 录制日志
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        # 直接跳转至登录后页面，前提是未登录用户访问待测系统会自动跳转至登录页面
        logged_page.goto("https://testwww.youpin898.com/stock?gameId=730&tabKey=1")

        # 判断是否成功进入系统，如果没有需要进行登录，一般在第一次访问系统，或登录信息过期等原因会触发
        if logged_page.is_visible(LoginPage.my_sale):
            print("已登录，直接开始用例执行")
        else:
            print("未登录，执行登录")
            logged_page.locator(LoginPage.login_but).click()
            logged_page.locator(LoginPage.phone_num).fill("15557993309")
            logged_page.locator(LoginPage.send_sms_but).click()
            logged_page.locator(LoginPage.input_sms).fill("888888")
            logged_page.locator(LoginPage.commit_but).click()
        yield logged_page

    # 测试执行结束后保存状态文件，前提是测试用例中不能退出系统，安全起见加上异常处理
    try:
        context.storage_state(path=ss_file)
    except Exception as e:
        print(e)


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html
