# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
from unittest import TestCase
from unittest.mock import Mock, patch

from dungeonstacks import entry_point
from dungeonstacks.io.display import Display


class TestEntryPoint(TestCase):
    def test_default_display_created(self):
        # pylint: disable=no-self-use
        with patch('dungeonstacks.Display') as mock:
            entry_point()
            mock.assert_called_once_with()

    def test_display_prints_message(self):
        # pylint: disable=no-self-use
        with patch('dungeonstacks.Display') as mock:
            display = Mock(spec=Display)
            mock.return_value = display
            entry_point()
            display.line.assert_called_once_with('Hello world')
