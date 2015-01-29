#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


install_requires = []
with open('requirements.txt') as f:
    for line in f:
        install_requires.append(line)


setup(
    name='helios',
    version='0.1.0',
    description='',
    url='https://github.com/pmcilwaine/helios',
    author='Paul Mcilwaine',
    author_email='paul.mcilwaine@gmail.com',
    install_requires=install_requires,
    packages=['helios', 'helios.admin']
)