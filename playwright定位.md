3.3、元素定位
官方文档：https://playwright.dev/python/docs/locators#lists

playwright推荐使用定位器也就是locators，定位器是自动等待与重试的核心能力。更符合用户行为的定位器。

这些是推荐的内置定位器。

page.get_by_role()通过显式和隐式可访问性属性定位。

page.get_by_text()按文本内容定位。
B
page.get_by_label()通过关联标签的文本查找表单控件。

page.get_by_placeholder()按占位符查找输入。

page.get_by_alt_text()通过其文本替代品定位元素，通常是图像。

page.get_by_title()通过标题属性定位元素。

page.get_by_test_id()根据其data-testid属性定位元素（可以配置其他属性）。
————————————————
page.locator("xpath=//h2")
page.locator("text=文本输入") 
page.locator("#s-usersetting-top")
page.locator("input[name=\"wd\"]").click()
page.get_by_role("button", name="百度一下").click()
page2.get_by_placeholder("唱片名、表演者、条码、ISRC").click()
page2.get_by_text("或者，亲自来帮豆瓣添加：").click()
playwright-python使用 evaluate() 方法来执行JavaScript脚本，和selenium类似，也有两种方法实现元素操作。

page.evaluate()：直接执行完整的JavaScript脚本。
locator.evaluate()：定位到元素后再使用JavaScript执行操作。
JS操作 ：page.evaluate('document.getElementsByClassName("ant-btn ant-btn-primary")[5].click()')

元素操作
下拉选择框：selectOpion、value、labei、index

文件上传：setInputFiles、单个文件、多个文件、拖放上传

鼠标点击：click、dbclick

鼠标拖动：down、up

鼠标移动：move

触摸屏幕：tag

键盘按键：press

截屏、录屏：screenshot、recordVideo

脚本录制：
-o 代表输出的代码文件的名称；--target 代表使用的语言，默认是 python，即会生成同步模式的操作代码，
如果传入 python-async 就会生成异步模式的代码；-b 代表的是使用的浏览器，默认是 Chromium，
其他还有很多设置，比如 --device 可以模拟使用手机浏览器，比如 iPhone 11，--lang 代表设置浏览器的语言，
--timeout 可以设置页面加载超时时间。
playwright codegen -o script.py -b firefox
 
python -m playwright codegen -o script.py -b firefox
