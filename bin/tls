#!/usr/bin/env python
# -*- coding: utf-8

import treepy

from treepy.mls_generation import MultiLS
from treepy.tree_generation import DisplayablePath

import os
import argparse

from pathlib import Path

def gen_mls_output(args):
    mls = MultiLS(args)
    mls.process()

    class mls_output:
        display_lines = mls.display_lines
        used_space = max([treepy.get_non_ANSI_line_length(line) for line in display_lines])
        used_lines = len(display_lines)

    return mls_output


def gen_treepy_output(args):
    root = args['path']
    DisplayablePath.load_args(args)
    paths = DisplayablePath.make_tree(Path(root))

    export_script_lines = ['#!/usr/bin/env bash'] # written to file only when -q flag is provided

    treepy_display_lines = []
    for path in paths:
        treepy_display_lines.append(path.displayable())
        export_script_lines.append('export {}{}=\"{}\"'.format(treepy.ENV_PREFIX,
                                                               path.num_paths - 1,
                                                               str(path.path.resolve())))

    if args['q']:
        with open(treepy.TEMP_FILE, 'w') as f:
            f.write('\n'.join(export_script_lines))

    class treepy_output:
        display_lines = treepy_display_lines
        used_space = max([treepy.get_non_ANSI_line_length(line) for line in display_lines])
        used_lines = len(display_lines)

    return treepy_output


def align_to_bottom(output1, output2):
    if output1.used_lines == output2.used_lines:
        return output1, output2
    elif output1.used_lines > output2.used_lines:
        output2.display_lines = [treepy.STYLIZE_BRANCHES('♬')] + [''] * (output1.used_lines - output2.used_lines - 1) + output2.display_lines
    elif output1.used_lines < output2.used_lines:
        output1.display_lines = [treepy.STYLIZE_BRANCHES('♬')] + [''] * (output2.used_lines - output1.used_lines - 1) + output1.display_lines

    return output1, output2


def main(args):
    terminal_width = int(os.popen('stty size', 'r').read().split()[1])
    lbuffer, mbuffer, rbuffer = 2, 3, 2
    usable_terminal_width = terminal_width - lbuffer - mbuffer - rbuffer

    if args['p']:
        args['max_text_width'] = int(usable_terminal_width * args['p'] / 100)
        mls_output = gen_mls_output(args)

        args['max_text_width'] = usable_terminal_width - mls_output.used_space
        treepy_output = gen_treepy_output(args)
    else:
        args['max_text_width'] = terminal_width
        treepy_output = gen_treepy_output(args)

        args['max_text_width'] = usable_terminal_width - treepy_output.used_space
        mls_output = gen_mls_output(args)

    mls_output, treepy_output = align_to_bottom(mls_output, treepy_output)

    tabulate = treepy.tabulate([['\n'.join(mls_output.display_lines),
                                 '\n'.join(treepy_output.display_lines)]], tablefmt=args['g'])

    print(treepy.STYLIZE_TABULATE_BORDER(tabulate))
    print(treepy.tabulate([['\n'.join(mls_output.display_lines),
                            '\n'.join(treepy_output.display_lines)]], tablefmt=args['g']))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()

    groupB = ap.add_argument_group('BOTH', 'Parameters relating to both treepy and mls')
    groupB.add_argument('path', nargs='?', default = os.getcwd(), help='Root directory. Default is working directory')
    groupB.add_argument('-a', action='store_true', help='Include those starting with `.`')
    groupB.add_argument('-p', type=float, default=None, help='percentage of terminal width taken up by mls. If not provided, treepy is prioritized')
    groupB.add_argument('-g', type=str, default='fancy_grid', help='A valid tabulate tablefmt string. E.g. `fancy_grid`, `plain`, `simple`')

    groupT = ap.add_argument_group('TREEPY', 'Parameters relating to treepy')
    groupT.add_argument('-d', action='store_true', help='Only display directories')
    groupT.add_argument('-f', action='store_true', help='Display the full path')
    groupT.add_argument('-q', action='store_true', help='Append quick-access variable path')
    groupT.add_argument('-D', default=10, type=int, help='Maximum depth, default 10')
    groupT.add_argument('-M', default=10, type=int, help='Max items to display per depth, default 10')
    groupT.add_argument('-A', action='store_true', help='Ignore parameters -D and -M')

    groupM = ap.add_argument_group('MLS', 'Parameters relating to mls')
    groupM.add_argument('-P', default=3, type=int, help='Number of parents to show (mls)')
    groupM.add_argument('-r', action='store_true', help='Use .. notation for paths relative to `path` (mls)')
    groupM.add_argument('-R', default=None, type=int, help='Max number of rows to display in each parent directory (mls)')

    args = ap.parse_args().__dict__

    if args['A']:
        args['D'] = None
        args['M'] = None

    main(args)
