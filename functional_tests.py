from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 在线待办应用首页:
        self.browser.get('http://localhost:8000')

        # 页面标题和头部都包含'To-Do'
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


# 其余注释...
if __name__ == '__main__':
    # 启动测试程序 与 禁止抛出ResourceWaring异常
    unittest.main(warnings='ignore')

# 输入一个待办事项
# 她在一个文本框中输入了 “ Buy peacock feathers ” （购买孔雀羽毛）

# 她按回车键后，页面更新了
# 待办事项表格中显示了 “ 1: Buy peacock feathers ”

# 页面中又显示了一个文本框，可以输入其他的待办事项
# 她输入了 “ Use peacock feathers to make a fly ” （使用孔雀羽毛做假蝇）

# 页面再次更新，她的清单中显示了这两个待办事项

# 伊迪丝想知道这个网站是否会记住她的清单
# 她看到网站为她生成了一个唯一的URL
# 而且页面中有一些文字解说这个功能
# 她访问那个URL，发现她的待办事项列表还在
