import unittest
import inventory

class TestInventory(unittest.TestCase):
    def setUp(self) -> None:
        self.inventory = inventory.StoreInventory()
        self.inventory_list = inventory.StoreInventory().inventory_list
        self.control_dict = {
            'name': 'Beef',
            'price': '2.29',
            'quantity': '3'
        }
        self.control_list = [
            {'name': 'Milk', 'price': '2.29', 'quantity': '2'},
            {'name': 'Eggs', 'price': '3.49', 'quantity': '3'},
            {'name': 'Cheese', 'price': '4.49', 'quantity': '1'},
            {'name': 'Bread', 'price': '$5.49', 'quantity': '4'}
        ]

    # test the method will return a dictionary if the name is not 
    # already in the list
    def test_add_item_correct(self):
        print('Enter correct input')
        self.assertEqual(self.control_dict, self.inventory.add_item())
    
    # checks method does not add dictionary to list if name already 
    # in the list
    def test_not_add_duplicate(self):
        print('Enter incorrect item')
        self.assertNotEqual(self.control_dict, self.inventory.add_item())

    # checks the method properly deletes the item in the list
    def test_delete_item(self):
        deleted_dict = {'name': 'Milk', 'price': '2.29', 'quantity': '2'}
        self.inventory.delete_item()
        self.assertNotIn(deleted_dict, self.inventory_list)

    # checks the method prints a message to 
    def test_not_delete_item(self):
        pass


if __name__ == '__main__':
    unittest.main()