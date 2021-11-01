from tests.signup import Signup


class AuthDefaultTest(Signup):

    def setUp(self):
        super().setUp()
        super().test_signup_full()
