from setuptools import setup, find_packages
import os
import pushnote

VERSION = pushnote.__version__

setup(
    name='pushnote',
    version=VERSION,
    license='GPL-2',
    description=('IPython magic function to send notifications wtih Pushbullet'),
    author='Nicholas Youngblut',
    author_email='nyoungb2@gmail.com',
    url='https://github.com/nick-youngblut/pushnote',
    packages=find_packages(exclude=[]),
    install_requires=['ipython'],
    long_description="""
An IPython magic extension for sending notifications with Pushbullet.
"""
)