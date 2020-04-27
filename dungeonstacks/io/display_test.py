# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from unittest import TestCase
from unittest.mock import call, Mock, patch

from dungeonstacks.io.display import Bullet, Display


class TestBulletMethods(TestCase):
    def test_none_function(self):
        self.assertEqual(Bullet.none(121, 'kaljsdf'), '')

    def test_index(self):
        for index in range(20):
            with self.subTest(index=index):
                result = Bullet.index(index, '90flkqje')
                self.assertEqual(result, str(index) + ' ')

    def test_fixed(self):
        sample = '948j21gklh2'
        fixed = Bullet.fixed(sample)
        result = fixed(9492, '19078197109740jlsk')
        self.assertEqual(result, sample)


class TestDisplayMethods(TestCase):
    def test_print_line_sends_to_regular_print(self):
        # pylint: disable=no-self-use
        with patch('dungeonstacks.io.display.print') as mock:
            sample = '847y12fnoiu2hv087erhq'
            Display().line(sample)
            mock.assert_called_once_with(sample)

    def test_print_list_on_plain_list(self):
        display = Display()
        with patch.object(display, 'line') as mock:
            items = ['9130810', 'japfhy7queh', 'JH89HpuhpYHpiug']
            display.list(items)
            calls = [call(item) for item in items]
            self.assertEqual(mock.call_args_list, calls)

    def test_print_list_with_bullet_function(self):
        display = Display()
        items = ['91071jufj', 'jasdhf;', '94e0jf']
        prefixes = ['jvne', 'l;aj*j;kj3/z', '940jf<)(#.>']
        answer = [call(p+s) for p, s in zip(prefixes, items)]
        bullet = Mock()
        bullet.side_effect = prefixes

        with patch.object(display, 'line') as mock:
            display.list(items, bullet=bullet)
            self.assertEqual(mock.call_args_list, answer)
