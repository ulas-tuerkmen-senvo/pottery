#-----------------------------------------------------------------------------#
#   base.py                                                                   #
#                                                                             #
#   Copyright © 2015-2017, Rajiv Bakulesh Shah, original author.              #
#   All rights reserved.                                                      #
#-----------------------------------------------------------------------------#



import doctest
import sys
import unittest

from pottery.base import Base
from pottery.base import _default_redis



class TestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.redis = _default_redis

    def tearDown(self):
        tmp_key_pattern = Base._RANDOM_KEY_PREFIX + '*'
        tmp_keys = self.redis.keys(pattern=tmp_key_pattern)
        self.redis.delete(tmp_keys)
        super().tearDown()



def run_doctests():
    results = doctest.testmod()
    sys.exit(bool(results.failed))
