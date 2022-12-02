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
            {'name': 'Bread', 'price': '5.49', 'quantity': '4'}
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

    # validates method will execute create_grid() when self.finished is false
    """@mock.patch('inventory.StoreInventory.create_grid')
    def test_start(self, mocked_create_grid):
        with mock.patch('inventory.StoreInventory.validate_input') as mocked_validate_input:
            control_inventory = inventory.StoreInventory()
            control_inventory.start_app()
            self.assertTrue(mocked_create_grid.called)"""

    # validates method will excecute help method when "HELP" is passed as an arguement
    @mock.patch('inventory.StoreInventory.help')
    def test_command_manager_help(self, mocked_help):
        control_inventory = inventory.StoreInventory()
        control_inventory.command_manager('HELP')
        self.assertTrue(mocked_help.called)

    # validates method will set value of self.finished to True
    def test_command_manager_done(self):
        control_inventory = inventory.StoreInventory()
        control_inventory.command_manager('DONE')
        self.assertTrue(control_inventory.finished)

    @mock.patch('inventory.StoreInventory.delete_item', return_value='Passed')
    def test_command_manager_delete(self, mocked_delete):
        with mock.patch('builtins.print') as mocked_print:
            control_inventory = inventory.StoreInventory()
            control_inventory.command_manager('DELETE')
            mocked_print.assert_called_with('Passed')

    # validates method will remove all items from the list when 'CLEAR' is passed as an arguement
    @mock.patch('builtins.print')
    def test_command_manager_clear(self, mocked_print):
        control_inventory = inventory.StoreInventory()
        control_inventory.command_manager('CLEAR')
        mocked_print.assert_called_with('cleared successfully')
        self.assertFalse(control_inventory.inventory_list)

    # validates method will execute the correct method when 'UPDATE' is passed as a parameter
    @mock.patch('inventory.StoreInventory.update_item')
    def test_command_manager_update(self, mock_update_item):
        control = inventory.StoreInventory()
        control.command_manager('UPDATE')
        self.assertTrue(mock_update_item.called)

    # validates method will execute the correct method when 'ADD' is passed as an arguement
    @mock.patch('inventory.StoreInventory.add_item')
    def test_command_manager_add(self, mock_add):
        control = inventory.StoreInventory()
        control.command_manager('ADD')
        self.assertTrue(mock_add.called)
    
    # validates method will collect user input and execute correct method when 'export' is passed as an arguement
    @mock.patch('builtins.input', return_value='inventory.csv')
    def test_command_manager_export(self, mock_input):
        with mock.patch('inventory.StoreInventory.csv_file_writer') as mock_csv_w:
            control = inventory.StoreInventory()
            control.command_manager('EXPORT')
            self.assertTrue(mock_csv_w.called)

    # validates method will collect user input and execute correct method when 'IMPORT' is passed as an arguement
    @mock.patch('builtins.input', return_value='new_inventory.csv')
    def test_command_manager_import(self, mock_input):
        with mock.patch('inventory.StoreInventory.csv_file_reader') as mock_csv_r:
            control = inventory.StoreInventory()
            control.command_manager('IMPORT')
            self.assertTrue(mock_csv_r.called)

    # validates method will execute correct method when 'PRINT' is passed as an arguement
    @mock.patch('inventory.StoreInventory.print_items')
    def test_command_manager_print(self, mock_print):
        control = inventory.StoreInventory()
        control.command_manager('PRINT')
        self.assertTrue(mock_print.called)

            

if __name__ == '__main__':
    unittest.main() 