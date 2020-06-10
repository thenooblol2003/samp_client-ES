#!/usr/bin/env python
from distutils.core import setup
try:
    long_description = open('README.md', 'r').read()
except:
    long_description = ''

setup(
    name='samp_client-ES',
    version='1.0.0',
    packages=['samp_client-ES'],
    url='https://github.com/thenooblol2003/samp_client-ES',
    license='None',
    author='Michal Dabski',
    author_email='contact@michaldabski.com',
    install_requires=['future'],
    description='SA-MP API client for python supporting both query and RCON APIs, plus, spanish decoding support',
    long_description=long_description,
)
