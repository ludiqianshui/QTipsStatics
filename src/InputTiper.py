import unittest


class InputTiper(object):

    def input_tiper_info (self, tiper_info):
        return

    def get_tiper_info (self):

        return


class Test (unittest.TestCase):
    def setUp(self):
        self.test_obj=InputTiper()

    def tearDown(self):
        self.test_obj = None

    def test_input_tiper(self):
        self.test_obj.get_tiper_info ()
        return 