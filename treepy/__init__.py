"""Bare-bones CLI for displaying a tree of file structure"""
__version__ = '0.1'

from pathlib import Path
from colored import fore, back, style

name = 'treepy'

ENV_PREFIX = 'TREE'

TEMP_FILE = Path.home() / '.treepy_temp.sh'

COLOR_DIR = fore.CYAN
STYLE_DIR = COLOR_DIR

COLOR_FILE = fore.ORANGE_RED_1
STYLE_FILE = COLOR_FILE

COLOR_MORE = fore.CORNSILK_1
STYLE_MORE = COLOR_MORE

COLOR_BRANCHES = fore.LIGHT_GOLDENROD_2C
STYLE_BRANCHES = COLOR_BRANCHES + style.BOLD

COLOR_DIR_HEADER = fore.CORNSILK_1 + back.DEEP_SKY_BLUE_4A
STYLE_DIR_HEADER = COLOR_DIR_HEADER

COLOR_QUICKACCESS = fore.GREY_42
STYLE_QUICKACCESS = COLOR_QUICKACCESS

STYLE_RESET = style.RESET

STYLIZE_DIR = lambda string: STYLE_DIR + string + STYLE_RESET
STYLIZE_FILE = lambda string: STYLE_FILE + string + STYLE_RESET
STYLIZE_MORE = lambda string: STYLE_MORE + string + STYLE_RESET
STYLIZE_BRANCHES = lambda string: STYLE_BRANCHES + string + STYLE_RESET
STYLIZE_DIR_HEADER = lambda string: STYLE_DIR_HEADER + string + STYLE_RESET
STYLIZE_QUICKACCESS = lambda string: STYLE_QUICKACCESS + string + STYLE_RESET
