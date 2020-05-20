# -*- coding: UTF-8 -*-
from distutils.core import setup
from setuptools import find_packages

import time  # noqa

_version = "0.1.dev-%s" % int(time.time())
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

setup(
    name='rootxnet-web',
    version=_version,
    packages=_packages,
    include_package_data=True,
    install_requires=[
        "Django==3.0.6",
        "jupyter==1.0.0",
        "gunicorn==20.0.4",
        "whitenoise==5.1.0",
    ],
)
