# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from unittest import TestCase
from unittest.mock import Mock

from dungeonstacks.game.page import Page, null_command, pop_command, replace_command


class StackCommandTestBase(TestCase):
    def setUp(self):
        self.original_stack = [Mock(spec=Page) for _ in range(3)]
        self.stack = self.original_stack.copy()
        self.page_a, self.page_b, self.page_c = self.stack


class TestStackCommandNull(StackCommandTestBase):
    def test_if_stack_is_unmodified(self):
        null_command(self.stack)
        self.assertListEqual(self.original_stack, self.stack)

    def test_if_none_is_returned(self):
        self.assertListEqual([], null_command(self.stack))


class TestStackCommandPop(StackCommandTestBase):
    def test_if_last_item_popped(self):
        pop_command(self.stack)
        self.assertListEqual(self.original_stack[:2], self.stack)

    def test_if_old_top_is_returned(self):
        self.assertListEqual([self.page_c], pop_command(self.stack))


class TestStackCommandReplace(StackCommandTestBase):
    def setUp(self):
        super(TestStackCommandReplace, self).setUp()
        self.new_top = Mock(spec=Page)
        self.command = replace_command(self.new_top)

    def test_if_top_of_stack_is_new_page(self):
        self.command(self.stack)
        self.assertEqual(self.stack[-1], self.new_top)
        self.assertEqual(self.stack[:-1], self.original_stack[:-1])

    def test_if_old_top_returned(self):
        result = self.command(self.stack)
        self.assertListEqual(result, [self.page_c])
