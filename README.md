# treepy
Bare-bones CLI for displaying a tree of file structure

99.9% of this very bare-bones utility is taken from [this stackoverflow answer](https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python/49912639#49912639). Thanks to the user [abstrus](https://stackoverflow.com/users/2479038/abstrus) for providing it.

## Usage

A couple of cases.

### Getting help

```
>>> treepy h
usage: treepy_python [-h] [-d] [-a] [-q] [-f] path

positional arguments:
  path        brief description

optional arguments:
  -h, --help  show this help message and exit
  -d          Only display directories
  -a          Include those starting with `.`
  -q          Append quick-access variable path
  -f          Display the full path
```

### Default dir is `.` if none is provided
```
>>> treepy
treepy/
├── bin/
│   ├── treepy
│   └── treepy_python
├── build/
│   ├── bdist.macosx-10.12-x86_64/
│   ├── lib/
│   │   └── treepy/
│   │       ├── __init__.py
│   │       └── tree_generation.py
│   └── scripts-3.6/
│       ├── treepy
│       └── treepy_python
├── dist/
│   └── UNKNOWN-0.1-py3.6.egg
├── LICENSE
├── README.md
├── requirements.txt
├── setup.cfg
├── setup.py
├── treepy/
│   ├── __init__.py
│   ├── __pycache__/
│   └── tree_generation.py
└── UNKNOWN.egg-info/
    ├── dependency_links.txt
    ├── PKG-INFO
    ├── requires.txt
    ├── SOURCES.txt
    └── top_level.txt
```

### Directories only

```
>>> treepy /Users/evan/Software/treepy/ -d
treepy/
├── bin/
├── build/
│   ├── bdist.macosx-10.12-x86_64/
│   ├── lib/
│   │   └── treepy/
│   └── scripts-3.6/
├── dist/
├── treepy/
│   └── __pycache__/
└── UNKNOWN.egg-info/
```

### Display full paths

```
>>> treepy -df
/Users/evan/Software/treepy/
├── /Users/evan/Software/treepy/bin/
├── /Users/evan/Software/treepy/build/
│   ├── /Users/evan/Software/treepy/build/bdist.macosx-10.12-x86_64/
│   ├── /Users/evan/Software/treepy/build/lib/
│   │   └── /Users/evan/Software/treepy/build/lib/treepy/
│   └── /Users/evan/Software/treepy/build/scripts-3.6/
├── /Users/evan/Software/treepy/dist/
├── /Users/evan/Software/treepy/treepy/
│   └── /Users/evan/Software/treepy/treepy/__pycache__/
└── /Users/evan/Software/treepy/UNKNOWN.egg-info/
```

### Create environmental variables of paths for quick access

For this, it is **essential** that the command is run as `source treepy`, otherwise environmental variables will not be retained in the shell you run `treepy` from.

```
>>> source treepy -dq
treepy/ → $TREE1
├── bin/ → $TREE2
├── build/ → $TREE3
│   ├── bdist.macosx-10.12-x86_64/ → $TREE4
│   ├── lib/ → $TREE5
│   │   └── treepy/ → $TREE6
│   └── scripts-3.6/ → $TREE7
├── dist/ → $TREE8
├── treepy/ → $TREE9
│   └── __pycache__/ → $TREE10
└── UNKNOWN.egg-info/ → $TREE11

>>> echo $TREE1
/Users/evan/Software/treepy
```
