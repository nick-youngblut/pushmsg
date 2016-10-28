from setuptools import setup, find_packages
import os
import pushmsg

VERSION = pushmsg.__version__

install_reqs = [
'ipython',
'configparser',
'pushbullet.py>=0.10.0'
]

setup(
    name='pushmsg',
    version=VERSION,
    license='MIT',
    description=('IPython magic function to send notifications wtih Pushbullet'),
    author='Nicholas Youngblut',
    author_email='nyoungb2@gmail.com',
    url='https://github.com/nick-youngblut/pushmsg',
    packages=find_packages(exclude=[]),
    install_requires=install_reqs,
    long_description="""
An IPython magic extension for sending notifications with Pushbullet.
It is useful for setting notfications for the completion of long jobs.
"""
)
