import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='library-management-system',
    version='0.1',
    packages=['libmgmt'],
    description='A Library managment system',
    long_description=README,
    author='Rohit Kashyap',
    author_email='x20196601@student.ncirl.ie',
    url='https://github.com/rohit-git-bot/CPP_.git',
    license='NCI',
    install_requires=[
        'Django>=1.6,<1.7',
    ]
)