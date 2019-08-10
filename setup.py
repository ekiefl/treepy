import os
from setuptools import setup, find_packages

setup(
    name='treepy',
    version="0.6",
    packages=find_packages(),
    author_email = 'kiefl.evan@gmail.com',
    author = 'Evan Kiefl',
    url = 'https://github.com/ekiefl/treepy',
    install_requires = [
        'argparse',
        'tabulate',
        'colored'
    ],
    scripts = [os.path.join('bin', 'treepy'),
               os.path.join('bin', 'treepy_python'),
               os.path.join('bin', 'tls'),
               os.path.join('bin', 'tls_python'),
               os.path.join('bin', 'mls'),
               os.path.join('bin', 'mls_python'),
    ],
)
