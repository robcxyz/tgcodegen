#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for cli"""
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import os
import hcl

import pytest

from pprint import pprint

TEST_TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')
TEST_STACKS_DIR = os.path.join(os.path.dirname(__file__), 'stacks')

COMMON_STACKS_DIR = os.path.join(os.path.dirname(__file__), '..', 'stacks')

# Name, valid or not valid boolean
STACK_FIXTURES = [
    (
        "common.hcl",
        False,
    ),
    (
        "common-render.hcl",
        False,
    ),
    (
        "basic-p-rep.hcl",
        False,
    ),
    (
        "bad-hcl.hcl",
        True,
    ),
    (
        "bad-common.hcl",
        True,
    )
]

# Name, valid or not valid boolean
HEAD_FIXTURES = [
    (
        "head",
        False
    ),
    (
        "bad-head",
        True,
    )
]

SERVICE_FIXTURES = [
    (
        "service",
        False
    ),
    (
        "bad-service",
        True,
    )
]

VERSION_FIXTURES = [
    "0.12", "0.11"
]

