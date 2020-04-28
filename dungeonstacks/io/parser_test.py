# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
from unittest import TestCase
from unittest.mock import call, Mock, patch

from dungeonstacks.io.display import Display
from dungeonstacks.io.parser import InputParser

INPUT_STR = 'dungeonstacks.io.parser.input'


class InputParserTester(TestCase):
    def setUp(self):
        self.display = Mock(spec=Display)
        self.input = InputParser(self.display)


@patch(INPUT_STR)
class TestParserAnyString(InputParserTester):
    def test_can_return_empty_string(self, mock):
        mock.return_value = ''
        self.assertEqual(self.input.any_string(), '')

    def test_prompt_passed_to_display_only(self, mock):
        prompt = '09haouihbjvjerhu ap dvhj ajdf'
        mock.return_value = ''
        self.input.any_string(prompt)

        mock.assert_called_once_with()
        self.display.line.assert_called_once_with(prompt)

    def test_display_not_called_when_prompt_is_empty(self, mock):
        mock.return_value = ''
        self.input.any_string()
        self.display.line.assert_not_called()

    def test_string_input_is_returned(self, mock):
        value = '9ngjbapuhjvn haeph fkhd'
        mock.return_value = value
        self.assertEqual(self.input.any_string(), value)


@patch(INPUT_STR)
class TestParserGetTypeMethod(InputParserTester):
    def test_can_return_string(self, mock):
        value = '9i0j2efpiohj'
        mock.return_value = value
        self.assertEqual(self.input.get_type(str), value)

    def test_returns_none_when_fails_with_no_retry(self, mock):
        mock.return_value = 'What'
        self.assertIsNone(self.input.get_type(int))

    def test_returns_an_integer(self, mock):
        mock.return_value = '391'
        self.assertEqual(self.input.get_type(int), 391)

    def test_does_not_unnecessarily_retry(self, mock):
        mock.return_value = '984'
        self.input.get_type(int, prompt='Integer', retry=True)
        self.display.line.assert_called_once_with('Integer')

    def test_retries_until_success(self, mock):
        mock.side_effect = ['Butter', 'Not It!', '1621']
        self.input.get_type(int, prompt='Try It', retry=True,
                            retry_string='Try Harder')
        self.assertEqual(
            self.display.line.call_args_list,
            [
                call('Try It'),
                call('Try Harder'),
                call('Try Harder'),
            ]
        )
