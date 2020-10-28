import unittest
from Api_Yandex import add_folder

class Test_API_Yandex(unittest.TestCase):

    def test_response(self):
        self.assertEqual(add_folder(),201)

class Test_negativ_API(unittest.TestCase):

    def test_folder_exists(self):
        self.assertEqual(add_folder(),409)

    def test_wrong_token(self):
        token = 'qwd3'
        self.assertEqual(add_folder(token),401)
