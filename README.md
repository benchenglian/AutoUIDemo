# AUtoUIDemo
极客时间UI自动化用例Demo；
语言：python 3.9.7
工具：selenium 4.1.0
测试框架：pytest 6.2.5
报告工具：Allure

# python包、文件说明
## config

config.ini存储被测系统的url和要启动的浏览器信息。
browser_engine.py文件读取该文件信息，启动浏览器，打开被测系统页面。

## data

存储被测系统用到的文件，如：上传或下载的文件。

## framework

- annotations.py 自定义的装饰器，写到次文件；如：失败后截图。
- base_page.py 二次封装selenium的一些操作，如：定位元素、点击、录入、获取元素text等等。把其看作：对象库层的一部分
- browser_engine.py 浏览器引擎，读取config.ini文件内容，打开浏览器访问被测系统页面。
- logger.py logging库的一些配置，指定保存日志的文件路径，日志级别，以及调用文件；将日志存入到指定的文件中。

## logs

脚本执行后产生的日志均存在该文件下。

## pageobjects 各页面把其看作：对象库层的一部分，和逻辑层

封装系统各页面，定位信息和操作；继承base_page中的BasePage类；
"""
    # 录入用户名
    username = 'xpath=>//*[@name="username"]' #用户名文本框
    def enter_username(self, text):
        self.enter(self.username,text)

    # 录入密码
    password = 'xpath=>//*[@id="password"]' # 密码
    def enter_password(self,text):
        self.enter(self.password,text)
"""
"""
    # 登录的逻辑，也可以把他放到testase中。
    def login(self, username, password):
        """
        登录
        :param username:
        :param password:
        :return:
        """
        self.enter(self.username, username)
        self.enter(self.password, password)
        self.click_element(self.login_btn)
"""

## testcase 业务层和数据层

测试pageobjects封装好的系统页面，所有文件以test_开头，里面的测试类也要以test开头或包含test（为了pytest框架能够识别）
所有的断言、参数化、业务逻辑在这里实现。


## report
xml报告和html报告生成的文件夹。

## screenshots
错误截图生成的文件夹，如果有图片对比的用例，母图也存在此处。

## tools
浏览器驱动存储。
下载地址：http://chromedriver.storage.googleapis.com/index.html

## 根目录下的文件
- conftest.py pytest独有的文件，主要做初始化浏览器和关闭浏览器。比如：可以使用fixture机制，实现打开浏览器并完成登录操作。
- msg_push.py 推送消息文件
- run_case.py 运行测试用例的文件。
- requirements.txt 各插件版本运行pip install -r requirements.txt进行安装
