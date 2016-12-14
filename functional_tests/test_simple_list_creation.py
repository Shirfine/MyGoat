from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class NewVistorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 在线待办应用首页:
        self.browser.get(self.server_url)

        # 页面标题和头部都包含'To-Do'
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请伊迪斯输入一个待办事项
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在文本框中输入'Buy peacock feathers'购买孔雀羽毛
        inputbox.send_keys('Buy peacock feathers')

        # 她按回车键后, 被带到了一个新的URL
        # 待办事项表格中显示了'1: Buy peacock feathers'
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        # self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 她输入了 “ Use peacock feathers to make a fly ” （使用孔雀羽毛做假蝇）
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新，她的清单中显示了这两个待办事项
        # self.check_for_row_in_list_table('1: Buy peacock feathers')
        # self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # 现在有一个叫做弗朗西斯的新用户访问啦网站

        ## 我们使用一个新浏览器会话
        ## 确保前一个用户待信息不会从cookie中泄漏出来
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # 弗朗西斯访问首页
        # 页面中看不到伊迪斯待清单
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # 弗朗西斯输入一个新待办事项, 新建一个清单
        # 他不像伊迪斯那样兴趣盎然
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # 弗朗西斯获得啦她待唯一URL
        francis_list_url = self.browser.current_url
        # self.assertRegex(francis_list_url, '/lists/.+')
        # self.assertNotEqual(francis_list_url, edith_list_url)

        # 这个也页面还是没有伊迪斯待清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', 'page_text')
        self.assertIn('Buy milk', page_text)

        # 伊迪丝想知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能
        self.fail('Finish the test!')

        # 她访问那个URL，发现她的待办事项列表还在
