from tests.default import DefaultTest
from tests.signup import Signup


class AuthDefaultTest(DefaultTest):

    def setUp(self):
        super().setUp()
        Signup().test_signup_full()
