import unittest
import item

class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_create_dict_obj(self):
        control = item.Item(name='Milk', price='2.29', quantity='3')
        control_dict = {'name': 'Milk', 'price': '2.29', 'quantity': '3'}
        self.assertEqual(control_dict, control.create_dict_obj())

if __name__ == '__main__':
    unittest.main()
