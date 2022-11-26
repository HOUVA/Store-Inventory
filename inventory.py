from item import Item

"""
Store Inventory
-----------------------------
A class for items in the store ✔
A class for the inventory ✔️
How can you add items to the inventory? ✔️
How can you update items in the inventory? ✔️
What about deleting items? ✔️
"""

class StoreInventory: 
    inventory_list = [
        {'name': 'Milk', 'price': '2.29', 'quantity': '2'},
        {'name': 'Eggs', 'price': '3.49', 'quantity': '3'},
        {'name': 'Cheese', 'price': '4.49', 'quantity': '1'}
    ]
    finished = False

    def __init__(self) -> None:
        pass

    # Runs the app
    def start_app(self):
        while not self.finished:
            self.create_grid()
            self.get_command()
        self.create_grid()

    
    def create_grid(self):
        print('     ---Inventory--- \n')
        print('Name      | Price  | Qty ')
        print('-----------------------')
        if self.inventory_list:
            for item in self.inventory_list:
                print(item['name'] + ' ' * (10 - len(item['name'])) + '|' + 
                      ' $' + item['price'] + '  |' + 
                      ' ' + item['quantity'] + '  |')
            print(self.sum_of_items())
        
    # Takes user input and depending on the value, executes the correct method.
    def get_command(self):

        command = input('\nCommand: ').upper()
        if command.__contains__('HELP'):
            self.help()
        if command.__contains__('DONE'):
            self.finished = True
        elif command.__contains__('DELETE'):
            if self.inventory_list:
                self.delete_item()
            else: 
                print('')
        elif command.__contains__('UPDATE'):
            if self.inventory_list:
                self.update_item()
            else:
                print('\nNo items to update\n')
        elif command.__contains__('ADD'):
            self.inventory_list.append(self.add_item())
        elif command.__contains__('PRINT'):
            self.export_items()
        else: 
            print('Not a valid option, type help for more info')

    # Support information on how the app works
    def help(self):
        help_text = open('help.txt', 'r')
        print(help_text.read())


    # creates a new dict object containing the name and price keys.
    # Item class creates the dict and can be called using create_dict_obj()
    def add_item(self): 
        new_item = Item(name=input('Name: ').capitalize(), price=input('Price: '), quantity=input('Quantity: '))
        checker = False

        # looks for a copy of the new item in the exisiting list
        # if a copy is found, tells the user to update the exisitng item
        for item in self.inventory_list:
            for key in item.keys():
                if item[key] == new_item.name:
                    checker = True
        if checker: 
            print('You already have that item in this List\nIf you want to update the current item, type update')
        else:
            return new_item.create_dict_obj()
    
    # changes either the name or price of the object selected
    # input is case sensitive
    def update_item(self):
        input_val = input('Which item would you like to update?: ')
        changed_val_type = input('What would you like to update? (name/price/quantity/both): ').lower()
        new_val = input("New Value: ")

        for items in self.inventory_list:
            for key in items.keys(): 
                if input_val in items[key]:
                    items[changed_val_type] = new_val


    # Removes an Item dict object from the list, based on the user key input value
    def delete_item(self):
        input_val = input('Which item would you like to delete?: ')
        for item in self.inventory_list:
            if input_val in item['name']:
                del self.inventory_list[self.inventory_list.index(item)]

    # adds the price values for each dict object and displays the total at the 
    # bottom of the list
    def sum_of_items(self):
        total = 0
        for item in self.inventory_list:
            total += float(item['price']) * int(item['quantity'])
        total = round(total, 2)
        return f'\nTotal: ${total}'
    
    # exports the dict object to a txt file
    def export_items(self):
        txt_file = open('inventory.txt', 'w')
        txt_file.write('        ---List---\n\n')
        for item in self.inventory_list:
                txt_file.write(item['name'] + ' ' * (10 - len(item['name'])) + '|' + 
                      ' $' + item['price'] + '  |' + 
                      ' ' + item['quantity'] + '  |')
                txt_file.write(self.sum_of_items())
        print('printed successfully!\n')
          

if __name__ == '__main__':
    inventory = StoreInventory()
    inventory.start_app()




