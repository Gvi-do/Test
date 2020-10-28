import unittest

from Secretary import get_people,get_shelf,get_document_list,add_document,documents,directories

class TestSomething(unittest.TestCase):

    def setUp(self):
        print('Test ')

    def test_get_people(self):
        self.assertEqual(get_people(documents,'10006'),'Аристарх Павлов')

    def test_add_document(self):
        self.assertEqual(add_document(),4)



