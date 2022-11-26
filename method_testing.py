import item
import inventory

class TestMethods: 
    
    def __init__(self) -> None:
        self.inventory_list = inventory.StoreInventory().inventory_list
        self.inventory_item = item.Item(name='Milk', price='2.29', quantity='4')
        pass
    
    def dict_iteration_test(self):
        for object in self.inventory_list: 
            for key, value in object.items():
                print(key)
                print(value)

    def add_item_test(self):
        for item in self.inventory_list:
            for key in item.keys():
                if item[key] == self.inventory_item.name:
                    print('found a match for {}'.format(self.inventory_item.name))
                else: 
                    print('did not find a match')
        self.inventory_list.append(self.inventory_item.create_dict_obj())

    def update_item(self, input_val, changed_val_type, new_val):
        for items in self.inventory_list:
            for key in items.keys(): 
                if input_val in items[key]:
                    items[changed_val_type] = new_val
    
if __name__ == '__main__':
    TestMethods().add_item_test()