自动等待及元素执行方法
操作元素的一系列方法，只要调用了测试夹函数page，就能引出操作元素的方法：

import pytestfrom playwright.sync_api import Pagedef test_example(page: Page):    page.goto("https://www.baidu.com")    page.hover('//*[@id="u1"]/*[text()="设置"]')    page.click('//*[@id="s-user-setting-menu"]//*[text()="搜索设置"]')    page.set_checked('//*[text()="全部语言"]', False)    assert page.title() == "百度一下，你就知道"    page.close()if __name__ == '__main__':    pytest.main(["-v", "test_example.py"])
playwright对元素执行前，会进行一系列可操作性检查，以确保这些行动按预期运行。它会自动等待所有相关检查通过，然后才执行请求的操作。如果所需的检查未在给定的范围内通过则抛出timeout，操作将失败并显示TimeoutError。

执行方法如下：

鼠标双击
    page.dblclick()

获取元素焦点
    # 获取元素并聚焦它。 如果没有匹配的元素，则方法等待匹配元素出现在 DOM 中。    page.focus('#su')

鼠标悬停
    # 就是鼠标放在按钮上，此方法针对那种浮框操作    page.hover('//*[@id="u1"]/*[text()="设置"]')

鼠标点击
    page.click('//*[@id="s-user-setting-menu"]//*[text()="搜索设置"]')

设置复选框取消或选中
    page.click('//*[@id="s-user-setting-menu"]//*[text()="搜索设置"]')

取消已选中复选框取
    # 确保元素是复选框或单选框。如果该元素已取消选中，则此方法立即返回    page.uncheck('//*[text()="仅简体中文"]')

输入参数
    # 此方法是聚焦元素，input输入值后触发事件。您也可以传递一个空字符串来清除输入字段。    page.fill("#kw", "秦时明月")

获取元素属性值
    # 返回元素属性值    page.get_attribute('#kw', 'name')

获取内部文本
    page.inner_text('//*[@id="s-hotsearch-wrapper"]//*[@data-index="2"]//*[@class="title-content-title"]')

获取内部HTML
    page.inner_html('//*[@id="s-hotsearch-wrapper"]//*[@data-index="2"]')

获取文本内容
    page.text_content('//*[@id="s-hotsearch-wrapper"]//*[@data-index="2"]')

截图
    # baidu.png存放至当前文件夹下的cases文件夹种    page.screenshot(path='./cases/baidu.png')

填写文本并触发键盘事件
    # 为文本中的每个字符发送一个keydown、keypress/input和keyup事件。    page.type("#kw", "hello")

输入键盘操作
    # 获取按钮元素，输入键盘操作    page.press('#su', 'Enter')

设置select下拉选项
    # 与值匹配的单个选择    page.select_option(/"select#colors/", /"blue/")    # 与标签匹配的单个选择    page.select_option(/"select#colors/", label=/"blue/")    # 多项选择    page.select_option(/"select#colors/", value=[/"red/", /"green/", /"blue/"])

调度事件
   # type可传："click", "dragstart"    page.dispatch_event('#su', 'click')

检查点（断言）

文字内容断言
    # 获取文本内容，进行断言    content = page.text_content('[target="_blank"]:first-child')    assert content == "新闻"

内部文字断言
    # 获取内部文字，进行断言    text = page.inner_text('[target="_blank"]:first-child')    assert text == "新闻"

属性断言
    # 获取属性值，进行断言    attribute = page.get_attribute('#su', 'value')    assert attribute == "百度一下"

复选框断言
    page.hover('//*[@id="u1"]/*[text()="设置"]')    page.click('//*[@id="s-user-setting-menu"]//*[text()="搜索设置"]')    # 复选框状态，进行断言    checked = page.is_checked('//*[text()="全部语言"]')    assert checked

js表达式断言
    # JS表达式，进行断言    js_content = page.locator('[data-index="4"]>a>[class="title-content-title"]').text_content()    assert js_content == "长津湖超战狼2成中国影史票房冠军"

内部HTML断言
    # 内部 HTML ，进行断言    html = page.inner_html('[class="hot-title"]')    assert "百度热搜" in html

元素可见断言
    # 元素可见性 ，进行断言    visible = page.is_visible('#su')    assert visible

启动状态断言
    # 启用状态（元素存在可点击） ，进行断言    enabled = page.is_enabled('#su')    assert enabled

直接对比断言
    assert page.title() == "百度一下，你就知道"
playwright还提供了自定义断言，这一块我还没有实操过，有兴趣可的可继续研究下：

# 断言本地存储值user_id = page.evaluate("() => window.localStorage.getItem('user_id')")assert user_id# 断言输入元素的值value = page.locator('#search').input_value()assert value == 'query'# 断言计算样式font_size = page.locator('div').evaluate('el => window.getComputedStyle(el).fontSize')assert font_size == '16px'# 断言列表长度length = page.locator('li.selected').count()assert length == 3

