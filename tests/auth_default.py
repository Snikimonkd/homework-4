import os

import mimesis
from steps.signup import SignupPage

from tests.default import DefaultTest


class AuthDefaultTest(DefaultTest):
    USEREMAIL = mimesis.Person().email()
    PASSWORD = os.environ['PASSWORD']
    USERENAME = 'Тестовое'

    def setUp(self):
        super().setUp()
        SignupPage().full()
