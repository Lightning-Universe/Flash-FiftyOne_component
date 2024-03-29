#!/usr/bin/env python

import os
from importlib.util import module_from_spec, spec_from_file_location

from setuptools import find_packages, setup

_PATH_ROOT = os.path.dirname(__file__)


def _load_py_module(fname, pkg="flash_fiftyone"):
    spec = spec_from_file_location(os.path.join(pkg, fname), os.path.join(_PATH_ROOT, pkg, fname))
    py = module_from_spec(spec)
    spec.loader.exec_module(py)
    return py


setup_tools = _load_py_module("setup_tools.py")

REQUIREMENTS = [req.strip() for req in open("requirements.txt").readlines()]

setup(
    name="flash_fiftyone",
    version="0.0.3",
    description="Run FiftyOne with Flash for Image Classification",
    author="Kushashwa Ravi Shrimali, Ethan Harris",
    author_email="kush@lightning.ai",
    url="https://github.com/Lightning-AI/LAI-flash-fiftyone-Component",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=setup_tools._load_requirements(_PATH_ROOT),
)
