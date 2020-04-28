
'''
A text based RPG with a continuous world between
characters. The world evolves between plays.
'''
from dungeonstacks.io.display import Display

def entry_point():
    '''
    Launches a default game in the cwd.
    '''
    display = Display()
    display.line('Hello world')
