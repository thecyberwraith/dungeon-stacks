# Dungeon Stacks

The idea is a text-based dungeon. The twist is that when a character dies or retires, the game world evolves in time for the next character based on your previous character's actions.

## General Setup
Simply run 'pipenv install' to install the program in a personal environment and then 'pipenv run dungeonstacks' to play the game.

## Development Setup

To prepare the development environment, run 'pipenv install --dev'. If developing with VSCode, then follow the instructions [here](https://olav.it/2017/03/04/pipenv-visual-studio-code/) to let VSCode know where your environment is. For this reason, the `settings.json` config file for VSCode will be ignored. Contributors should adhere to 100% test coverage and 10/10 pylint results for all committed code. Appropriate tasks to do this in your VSCode environment are supplied. 

Currently, a default launch json for Python debugging in VSCode is excluded, but it may be added later if debugging issues in Windows arise.
