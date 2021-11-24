# -*- coding: utf-8 -*-
import sys
import unittest
from cases.login import LoginTest
from cases.registration import RegistrationTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
            unittest.makeSuite(RegistrationTest)
            # unittest.makeSuite(LoginTest),
        )
    )

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
