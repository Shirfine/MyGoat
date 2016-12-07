from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # 伊迪斯访问首页,提交了一个空待办事项
        # 输入框中没有内容就按下了回车

        # 首页刷新了, 显示了一个错误消息
        # 提示待办事项不能为空

        # 她输入了一些文字, 再次提交就没问题了

        # 她又提交了个空待办事项
        # 在清单页面她看到了一个类似待错误消息
        # 输入文字后就没问题了
        self.fail('write me!')
