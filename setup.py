#!/usr/bin/env python

import os
import sys

from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py register sdist bdist_wheel upload')
    sys.exit()


setup(
    name='sentry_sso_google',
    version='0.1',
    description='Google SSO support for Sentry',
    author='Educreations Engineering',
    author_email='engineering@educreations.com',
    url='https://github.com/educreations/sentry-sso-google',
    install_requires=['sentry'],
    packages=["sentry_sso_google"],
    license="MIT",
)
