from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testwww.youpin898.com/")
    page.get_by_text("登录").click()
    page.get_by_placeholder("请输入手机账号").click()
    page.get_by_placeholder("请输入手机账号").fill("15557993309")
    page.get_by_role("button", name="获取验证码").click()
    page.locator("div").filter(has_text="发送成功").nth(2).click()
    page.get_by_text("发送成功").click()
    page.locator("div").filter(has_text="发送成功").nth(2).click()
    page.get_by_text("发送成功").click(click_count=5)
    page.get_by_placeholder("请输入短信验证码").click()
    page.get_by_placeholder("请输入短信验证码").fill("888888")
    page.get_by_role("button", name="登录/注册").click()
    page.get_by_role("link", name="我的库存").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
