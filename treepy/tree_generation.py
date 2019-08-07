#!/usr/bin/env python
# -*- coding: utf-8

import treepy

import os

from pathlib import Path
from colored import fore, back, style

class DisplayablePath(object):
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '
    num_paths = 0

    @classmethod
    def load_args(cls, args):
        cls.args = args

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        cls.num_paths += 1
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path
                               for path in root.iterdir()
                               if criteria(path)),
                          key=lambda s: str(s).lower())

        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                for obj in cls.make_tree(path, parent=displayable_root, is_last=is_last, criteria=criteria):
                    yield obj
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        if cls.args['d'] and not path.is_dir():
            return False

        if not cls.args['a'] and str(path.name).startswith('.'):
            return False

        return True

    @property
    def displayname(self):
        if self.args.get('f'):
            display = str(self.path.absolute())
        else:
            display = self.path.name

        if self.path.is_dir():
            display += '/'

        if self.args.get('q'):
            display = display + '{} → ${}{}{}'.format(fore.GREY_42, treepy.ENV_PREFIX, self.num_paths, style.RESET)

        return display

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))
