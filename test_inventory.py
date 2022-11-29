import unittest
from unittest import TestCase
from unittest import mock
import inventory

class TestInventory(TestCase):
    def setUp(self) -> None:
        self.inventory = inventory.StoreInventory()
        self.inventory_list = inventory.StoreInventory().inventory_list

        self.control_dicts = [{'name': 'Beef', 'price': '2.29','quantity': '3'},
                              {'name': 'Milk', 'price': '2.29', 'quantity': '2'}                 
        ]
        self.control_list = [
            {'name': 'Milk', 'price': '2.29', 'quantity': '2'},
            {'name': 'Eggs', 'price': '3.49', 'quantity': '3'},
            {'name': 'Cheese', 'price': '4.49', 'quantity': '1'},
            {'name': 'Bread', 'price': '$5.49', 'quantity': '4'}
        ]

    # validates method will return a dictionary if the name does not exist
    @mock.patch('builtins.input', side_effect=['Beef','2.29','3'])
    def test_add_item(self, mocked_input):
        self.inventory.add_item()
        self.assertIn(self.control_dicts[0], self.inventory_list)
    
    
    # validates method does not add dictionary to list if name already exists
    @mock.patch('builtins.input', side_effect=['Milk', '2.29', '3'])
    def test_add_item_duplicate(self):
        print('Enter incorrect item')
        self.assertNotEqual(self.control_dicts[0], self.inventory.add_item())

    # validates method will remove the dictionary object from the self.inventory list
    @mock.patch('builtins.input', return_value='Milk')
    def test_delete_item(self, mocked_input):
        inventory.StoreInventory().inventory_list = self.control_list
        self.inventory.delete_item()
        self.assertNotIn(self.control_dicts[1], inventory.StoreInventory().inventory_list)

    # validates method will return a string if the input passed is not found in name key in list
   # @mock.patch('inventory.input', side_effect='Milk')
    #def test_not_delete_item_not_in_list(self, mock_input):
    #   self.inventory_list = []
    #  self.assertEqual(self.inventory.delete_item(), 'Item not found in list')

if __name__ == '__main__':
    unittest.main()