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
        "Django==2.2.7",
        "jupyter==1.0.0",
        "gunicorn==20.0.3",
        "whitenoise==4.1.4",
    ],
)
