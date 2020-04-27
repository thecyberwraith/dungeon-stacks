'''
Class to handle all output to the user.
'''

from typing import Callable, List

BulletFunc = Callable[[int, str], str]


class Bullet:
    '''
    This is a static class which provides bullet methods (of type BulletFunc)
    to be used in the print_list function.
    '''
    @staticmethod
    def none(index: int, string: str) -> str:
        '''
        A BulletFunc that provides no bullet prefix.
        '''
        # pylint: disable=unused-argument

        return ''

    @staticmethod
    def index(index: int, string: str) -> str:
        '''
        A BulletFunc that provides an index prefix.
        '''
        # pylint: disable=unused-argument

        return str(index) + ' '

    @staticmethod
    def fixed(string: str) -> BulletFunc:
        '''
        This method *generates* a BulletFunc that simply returns the provided string.
        '''
        return lambda i, s: string


class Display:
    '''
    This class handles common text display functionality, so there should not
    be any print statements ANYWHERE else in my code.
    '''

    def line(self, line: str) -> None:
        '''
        Displays a single line to the user.
        '''
        # pylint: disable=no-self-use
        print(line)

    def list(self, string_list: List[str], bullet: BulletFunc = None) -> None:
        '''
        Displays a list of items, each on its own line.  The bullet option determines
        how the prefix will look. See the Bullet class methods for possible options.
        '''
        if bullet is None:
            bullet = Bullet.none

        for index, item in enumerate(string_list):
            self.line(f'{bullet(index, item)}{item}')
