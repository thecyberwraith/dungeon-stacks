'''
A single displayed page to the user. It receives a single input from the user,
and based on that input, dictates what page should then be displayed.
'''

from abc import abstractmethod, ABC
from typing import Callable, List

from dungeonstacks.io.display import Display
from dungeonstacks.io.parser import InputParser


StackCommand = Callable[[List['Page']], List['Page']]


class Page(ABC):
    '''
    A single unit that is displayed to the user. It has hooks for when to display
    and when to receive input.
    '''

    @abstractmethod
    def on_display(self, display: Display) -> None:
        '''
        A hook to display text to the user.
        '''

    @abstractmethod
    def on_input(self, parser: InputParser) -> StackCommand:
        '''
        A hook to receive input from the user. The return value is a command for
        which page should follow (or if the page should be destroyed).
        '''

    def on_remove(self) -> None:
        '''
        Hook to let the page know it's been removed from the page stack.
        '''


def null_command(stack: List[Page]) -> List[Page]:
    '''
    A command which does not modify the page stack.
    '''
    # pylint: disable=unused-argument
    return []


def pop_command(stack: List[Page]) -> List[Page]:
    '''
    A command that simply pops the current page off the stack.
    '''
    return [stack.pop(-1)]


def replace_command(new_page: Page):
    '''
    This command constructs a new StackCommand that replaces the top page with the page specified
    in the call.
    '''

    def specified_replace_command(stack: List[Page]) -> List[Page]:
        removed = stack.pop(-1)
        stack.append(new_page)
        return [removed]

    return specified_replace_command
