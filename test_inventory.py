import unittest
from unittest import TestCase
from unittest import mock
import inventory
import io

class TestInventory(TestCase):
    def setUp(self) -> None:

        self.control_dicts = [
            {'name': 'Beef', 'price': '2.29','quantity': '3'},
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
        control_inventory = inventory.StoreInventory()
        control_inventory.add_item()
        self.assertIn(self.control_dicts[0], control_inventory.inventory_list)
        mocked_input.side_effect = True
    
    
    # validates method does not add dictionary to list if name already exists
    @mock.patch('builtins.input', side_effect=['Beef', '2.29', '3'])
    def test_add_item_duplicate(self, mocked_input):
        with mock.patch('builtins.print') as mock_print:
            inventory.StoreInventory().inventory_list = self.control_list
            inventory.StoreInventory().add_item()
            mock_print.assert_called_with('You already have that item in this List\nIf you want to update the current item, type update')
            mocked_input.side_effect = True


    # validates method will remove the dictionary object from the self.inventory list
    @mock.patch('builtins.input', return_value='Milk')
    def test_delete_item(self, mocked_input):
        control_inventory = inventory.StoreInventory()
        control_inventory.inventory_list = self.control_list
        control_inventory.delete_item()
        self.assertNotIn(self.control_dicts[1], control_inventory.inventory_list)


    # validates method will return a string if the input passed is not found in name key in list
    @mock.patch('builtins.input', return_value='Beer')
    def test_not_delete_item_not_in_list(self, mock_input):
        with mock.patch('builtins.print') as mock_print:
            inventory.StoreInventory().inventory_list = self.control_list
            result = inventory.StoreInventory().delete_item()
            self.assertEqual('Item not found in list', result)


    # validates the method will return a string if the self.inventory_list is empty
    def test_not_delete_list_empty(self):
        control_inventory = inventory.StoreInventory()
        control_inventory.inventory_list = []
        result = control_inventory.delete_item()
        test_string = 'There is nothing to delete'
        self.assertEqual(test_string, result)


    # validates method will call the command_manager method if correct input is provided
    @mock.patch('inventory.StoreInventory.command_manager')
    def test_validate_input_correct(self, mocked_object):
        with mock.patch('builtins.input', return_value='Add') as mocked_input:
            control_inventory = inventory.StoreInventory()
            control_inventory.validate_input()
            self.assertTrue(mocked_object.called)


    # validates method will print message if incorrect input is provided 
    @mock.patch('builtins.input', return_value='Hello')   
    def test_validate_input_incorrect(self, mocked_input):
        with mock.patch('builtins.print') as mocked_print:
            control_inventory = inventory.StoreInventory()
            control_inventory.validate_input()
            control_print = 'Enter a valid input'
            mocked_print.assert_called_with(control_print)
        

if __name__ == '__main__':
    unittest.main()