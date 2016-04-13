#!/usr/bin/env python

import os
import sys

from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py register sdist bdist_wheel upload')
    sys.exit()


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()


setup(
    name='sentry-sso-google',
    version='1.2',
    description='Google SSO support for Sentry',
    long_description=readme,
    author='Educreations Engineering',
    author_email='engineering@educreations.com',
    url='https://github.com/educreations/sentry-sso-google',
    install_requires=['sentry>=7.5'],
    packages=["sentry_sso_google"],
    license="MIT",
)
