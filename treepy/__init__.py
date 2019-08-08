"""Bare-bones CLI for displaying a tree of file structure"""
__version__ = '0.1'

from pathlib import Path

name = 'treepy'

ENV_PREFIX = 'TREE'
TEMP_FILE = Path.home() / '.treepy_temp.sh'
