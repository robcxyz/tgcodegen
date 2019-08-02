# -*- coding: utf-8 -*-


from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import os

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



