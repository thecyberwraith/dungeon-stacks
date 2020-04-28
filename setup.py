'''
Setup file for dungeonstacks.

Currently requires no dependencies, and adds an executable
called 'dungeonstacks' to the path.
'''
import setuptools

setuptools.setup(
    name="dungeonstacks",
    description="A text based RPG with evolving world.",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'dungeonstacks=dungeonstacks:entry_point',
        ]
    }
)
