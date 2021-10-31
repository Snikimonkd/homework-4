#!/usr/bin/env python2

import sys
import unittest
from tests.auth import AuthTest
from tests.signup import SignupTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(SignupTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
