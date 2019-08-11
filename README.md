# treepy
Couple of command line utilities for visualizing filepaths in the context of their directory structure.

# Installation

**PyPI:**

```
pip install treepy
```

**git clone:**

```
git clone https://github.com/ekiefl/treepy.git
cd treepy
python setup.py install
treepy -h
```

# Usage

## 1. `treepy`

<img src="images/treepy_d.png" width="31%" align="center">

Visualize the file structure of a root directory. 99% of this bare-bones utility is taken from [this stackoverflow answer](https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python/49912639#49912639). Thanks to the user [abstrus](https://stackoverflow.com/users/2479038/abstrus) for providing it.


### `treepy -h` (getting help)

```
usage: treepy_python [-h] [-d] [-f] [-a] [-q] [-D D] [-M M] [-A] [path]

positional arguments:
  path        Root directory of tree. Default is working directory

optional arguments:
  -h, --help  show this help message and exit
  -d          Only display directories
  -f          Display the full path
  -a          Include those starting with `.`
  -q          Append quick-access variable path
  -D D        Maximum depth, default 10
  -M M        Max items to display per depth, default 10
  -A          Ignore parameters -D and -m (display all)
```

### `treepy` (most simple command)

```
treepy/
├── build/
│   ├── bdist.macosx-10.12-x86_64/
│   ├── lib/
│   │   └── treepy/
│   │       ├── mls_generation.py
│   │       ├── tree_generation.py
│   │       └── __init__.py
│   └── scripts-3.6/
│       ├── tls_python
│       ├── mls_python
│       ├── tls
│       ├── mls
│       ├── treepy_python
│       └── treepy
├── treepy.egg-info/
│   ├── requires.txt
│   ├── PKG-INFO
│   ├── top_level.txt
│   ├── dependency_links.txt
│   └── SOURCES.txt
├── images/
│   ├── mls_r.png
│   ├── tls.png
│   └── treepy_d.png
├── treepy/
│   ├── __pycache__/
│   │   ├── __init__.cpython-36.pyc
│   │   ├── multils_generation.cpython-36.pyc
│   │   ├── tree_generation.cpython-36.pyc
│   │   └── mls_generation.cpython-36.pyc
│   ├── tree_generation.py
│   ├── mls_generation.py
│   └── __init__.py
├── dist/
│   ├── treepy-0.6-py3.6.egg
│   └── treepy-0.5-py3.6.egg
├── bin/
│   ├── treepy_python
│   ├── tls_python
│   ├── treepy
│   ├── tls
│   ├── mls_python
│   └── mls
├── LICENSE
├── setup.py
├── README.md
└── setup.cfg
```


### `treepy -d` (directories only)

```
treepy/
├── build/
│   ├── bdist.macosx-10.12-x86_64/
│   ├── lib/
│   │   └── treepy/
│   └── scripts-3.6/
├── treepy.egg-info/
├── treepy/
│   └── __pycache__/
├── images/
├── dist/
└── bin/
```

### `treepy -df` (display full paths)

```
/Users/evan/Software/treepy/
├── /Users/evan/Software/treepy/build/
│   ├── /Users/evan/Software/treepy/build/bdist.macosx-10.12-x86_64/
│   ├── /Users/evan/Software/treepy/build/lib/
│   │   └── /Users/evan/Software/treepy/build/lib/treepy/
│   └── /Users/evan/Software/treepy/build/scripts-3.6/
├── /Users/evan/Software/treepy/treepy.egg-info/
├── /Users/evan/Software/treepy/treepy/
│   └── /Users/evan/Software/treepy/treepy/__pycache__/
├── /Users/evan/Software/treepy/images/
├── /Users/evan/Software/treepy/dist/
└── /Users/evan/Software/treepy/bin/
```

### `source treepy -dq` (quick-access environment variables)

For this, it is **essential** that the command is run as `source treepy`, otherwise environmental variables will not be retained in the shell you run `treepy` from.

```
treepy/ → $TREE0/
├── build/ → $TREE1/
│   ├── bdist.macosx-10.12-x86_64/ → $TREE2/
│   ├── lib/ → $TREE3/
│   │   └── treepy/ → $TREE4/
│   └── scripts-3.6/ → $TREE5/
├── treepy.egg-info/ → $TREE6/
├── treepy/ → $TREE7/
│   └── __pycache__/ → $TREE8/
├── images/ → $TREE9/
├── dist/ → $TREE10/
└── bin/ → $TREE11/
```

Each path in tree is stored as an environmental variable `TREE[X]`, where `[X]` is a number. Running

```
echo $TREE1
``` 

yields:

```
/Users/evan/Software/treepy/build
```

## 2. `mls`

<img src="images/mls_r.png" width="79%" align="center">

multi-`ls`. `ls` the contents of a directory as well as _n_ of its parent directories.

### `mls -h` (getting help)

```
usage: mls_python [-h] [-d] [-r] [-a] [-P P] [-R R] [path]

positional arguments:
  path        Root directory. Default is working directory

optional arguments:
  -h, --help  show this help message and exit
  -d          Only display directories
  -r          Use .. notation for paths relative to `path`
  -a          Include those starting with `.`
  -P P        Number of parents to show
  -R R        Max number of rows to display in each parent directory
```

### `mls` (most simple command)

```
▶ /Users/evan/Software/treepy/
treepy              images              LICENSE             setup.cfg
build               dist                setup.py
treepy.egg-info     bin                 README.md
▶ /Users/evan/Software/treepy/treepy/
__pycache__           tree_generation.py    mls_generation.py     __init__.py
▶ /Users/evan/Software/treepy/treepy/__pycache__/
__init__.cpython-36.pyc           tree_generation.cpython-36.pyc
multils_generation.cpython-36…     mls_generation.cpython-36.pyc
```

### `mls -r` (display paths with `..` notation)

```
▶ /Users/evan/Software/treepy/
../../treepy              ../../dist                ../../README.md
../../build               ../../bin                 ../../setup.cfg
../../treepy.egg-info     ../../LICENSE
../../images              ../../setup.py
▶ /Users/evan/Software/treepy/treepy/
../__pycache__           ../mls_generation.py
../tree_generation.py    ../__init__.py
▶ /Users/evan/Software/treepy/treepy/__pycache__/
./__init__.cpython-36.pyc         ./tree_generation.cpython-36.…
./multils_generation.cpython-…    ./mls_generation.cpython-36.p…
```

### `mls -R 2` (max rows to display per parent)

```
▶ /Users/evan/Software/treepy/
treepy              treepy.egg-info     dist                LICENSE
build               images              bin                 setup.py
…
▶ /Users/evan/Software/treepy/treepy/
__pycache__           tree_generation.py    mls_generation.py     __init__.py
▶ /Users/evan/Software/treepy/treepy/__pycache__/
__init__.cpython-36.pyc           tree_generation.cpython-36.pyc
multils_generation.cpython-36…     mls_generation.cpython-36.pyc
```

### `mls -p 2` (parents to show)

```
▶ /Users/evan/Software/treepy/treepy/
__pycache__           tree_generation.py    mls_generation.py     __init__.py
▶ /Users/evan/Software/treepy/treepy/__pycache__/
__init__.cpython-36.pyc           tree_generation.cpython-36.pyc
multils_generation.cpython-36…     mls_generation.cpython-36.pyc
```

## 3. `tls`

<img src="images/tls.png" width="79%" align="center">


