import sys
import time
from time import sleep
from playwright.async_api import Dialog
from seldom.testdata.conversion import json_to_list
from page.login_page import LoginPage
import allure
import pytest
from common.config import *
from playwright.sync_api import Playwright, sync_playwright, expect


@allure.feature('登录测试')
class TestLogin:
    @pytest.mark.parametrize(
        "phone, code",
        json_to_list(data_path + "/login_data.json")
    )
    @allure.story("test001-登录-成功")
    def test_login_001(self, login_page,phone,code, base_url):
        # 跳转有品首页
        login_page.goto(base_url)
        # 点击登录按钮
        login_page.locator(LoginPage.login_but).click()
        # 点击手机号输入框
        login_page.locator(LoginPage.phone_num).click()
        # 输入手机号
        login_page.locator(LoginPage.phone_num).fill(phone)
        # 点击发送验证码
        login_page.locator(LoginPage.send_sms_but).click()
        # 点击验证码输入框
        login_page.locator(LoginPage.input_sms).click()
        # 输入验证码
        login_page.locator(LoginPage.input_sms).fill(code)
        # 有时登录频繁需要滑动验证码

        dropbutton = login_page.locator(LoginPage.veriy)
        if login_page.is_visible(LoginPage.veriy):
            # 获取拖动按钮位置并拖动
            box = dropbutton.bounding_box()

            login_page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2)

            login_page.mouse.down()

            mov_x = box['x'] + box['width'] / 2 + 260

            login_page.mouse.move(mov_x, box['y'] + box['height'] / 2)

            login_page.mouse.up()
        else:
            pass

        # 点击登录/注册按钮
        login_page.locator(LoginPage.commit_but).click()

        # 登录后会展示我的出售、我的库存按钮，这个获取我的出售元素值
        content = login_page.text_content(LoginPage.my_sale)
        # 断言
        assert "我的出售" in content
