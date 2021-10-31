#!/usr/bin/env python2

import sys
import unittest
from tests.auth import Auth
from tests.signup import Signup, Presettings


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(Auth),
        unittest.makeSuite(Signup),
        unittest.makeSuite(Presettings),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
