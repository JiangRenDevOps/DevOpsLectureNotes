#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from setuptools import setup, find_packages

setup(
    name='devops-cli',
    version='0.1-dev',
    license='MIT',
    description='DevOps Tool',
    author='Yu Wang',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    install_requires=[
        'click==7.0',
        'click-repl==0.1.6'
    ],
    entry_points={
        'console_scripts': [
            'devops-cli = cli_tool.click_demo:process',
        ]
    },
)
