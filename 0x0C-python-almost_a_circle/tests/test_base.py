import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_base_instance(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_base_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_string(self):
        # Add your test cases for to_json_string method
        pass

    def test_save_to_file(self):
        # Add your test cases for save_to_file method
        pass

    def test_from_json_string(self):
        # Add your test cases for from_json_string method
        pass

    def test_create(self):
        # Add your test cases for create method
        pass

    def test_load_from_file(self):
        # Add your test cases for load_from_file method
        pass


if __name__ == '__main__':
    unittest.main()
