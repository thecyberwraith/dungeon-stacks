'''
Handles parsing of user input into program usable content. The core implementation
falls under the InputParser class.
'''
from typing import Type

from dungeonstacks.io.display import Display


class InputParser:
    '''
    Gathers information from the user, usually accompanied by a prompt.
    '''

    def __init__(self, display: Display):
        '''
        Constructs a InputParser whose prompts are displayed on the provided display.
        '''
        self._display = display

    def any_string(self, prompt: str = None) -> str:
        '''
        Returns exactly what the user provides without any retries or conversions.
        '''
        if prompt is not None:
            self._display.line(prompt)

        return input()

    def get_type(self, type_cast: Type, prompt: str = None,
                 retry: bool = False, retry_string: str = None):
        '''
        Attempts to cast the provided string input from the user into the request
        type by calling the type variable with the string input. If prompt is
        provided, then that is first displayed to the user.

        If retry is set to True, then the program will continuously loop until
        type no longer casts a ValueError. Otherwise, if a ValueError is thrown,
        this method returns None. If a retry_string is provided, then it is
        displayed every time the user provided invalid input.
        '''
        # Dev Note: This is a little more convoluted than necessary, but it
        # makes things explicit while also appeasing coverage
        cast_error = False
        value = None

        try:
            value = type_cast(self.any_string(prompt))
        except ValueError:
            cast_error = True

        while cast_error and retry:
            try:
                value = type_cast(self.any_string(retry_string))
                cast_error = False
            except ValueError:
                cast_error = True

        return value
