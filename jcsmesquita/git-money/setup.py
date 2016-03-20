#The following needs to be run in the command line to add the gitmoney interface:
#sudo pip3 install --editable .

from setuptools import setup

setup(
    name = 'gitmoney',
    version = '0.1',
    py_modules = ['gitmoney'],
        install_requires=[
            'Click',
            'commonregex',
    ],
    entry_points={
        'console_scripts': [
            'gitmoney = app.cli:cli',
        ]
    }
)
