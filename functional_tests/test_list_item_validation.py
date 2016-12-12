from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # 伊迪斯访问首页,提交了一个空待办事项
        # 输入框中没有内容就按下了回车
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # 首页刷新了, 显示了一个错误消息
        # 提示待办事项不能为空
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 她输入了一些文字, 再次提交就没问题了
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # 她又提交了个空待办事项
        self.get_item_input_box().send_keys('\n')

        # 在清单页面她看到了一个类似待错误消息
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 输入文字后就没问题了
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

