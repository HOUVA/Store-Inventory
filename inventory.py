from item import Item
import csv

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
        {'name': 'Milk', 'price': '2.29', 'quantity': '3'}
    ]
    finished = False
    command_options = ['HELP', 'DONE', 'ADD', 'DELETE', 'CLEAR', 
                       'UPDATE', 'IMPORT', 'EXPORT', 'PRINT']


    # Runs the app
    def start_app(self):
        while not self.finished:
            self.create_grid()
            self.validate_input()
        self.create_grid()

    # Creates a grid in the terminal
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
        
    def validate_input(self): 
        command = input('\nCommand: ').upper()

        if command in self.command_options:
            self.command_manager(command)
        else: 
            print('Enter a valid input')
        


    # Takes user input and depending on the value, executes the correct method.
    def command_manager(self, command):
        if command.__contains__('HELP'):
            self.help()
        if command.__contains__('DONE'):
            self.finished = True
        elif command.__contains__('DELETE'):
            print(self.delete_item())
        elif command.__contains__('CLEAR'):
            if self.inventory_list:
                self.clear_items()
            else: 
                print('Your list is already empty')
        elif command.__contains__('UPDATE'):
            if self.inventory_list:
                self.update_item()
            else:
                print('\nNo items to update\n')
        elif command.__contains__('ADD'):
            self.add_item()
        elif command.__contains__('EXPORT'):
            answ = input('Type the file you would like to export to: ')
            self.csv_file_writer(answ)
        elif command.__contains__('IMPORT'):
            answ = input('Type the file you would like to import: ')
            self.inventory_list = self.csv_file_reader(answ)
        elif command.__contains__('PRINT'):
            self.print_items()


    # Support information on how the app works
    def help(self):
        help_text = open('help.txt', 'r')
        print(help_text.read())


    # creates a new dict object containing the name and price keys.
    # Item class creates the dict and can be called using create_dict_obj()
    def add_item(self): 
        name = input('Name: ').capitalize()
        price = input('Price: ')
        quantity = input('Quantity: ')
        checker = False
        for item in self.inventory_list:
            for key in item.keys():
                if item[key] == name:
                    checker = True
        if checker: 
            print('You already have that item in this List\nIf you want to update the current item, type update')
        else:
            self.inventory_list.append(Item(name=name,price=price,quantity=quantity).create_dict_obj())
    

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
        input_val = input('Which item would you like to delete?: ').capitalize()
        if self.inventory_list:
            for item in self.inventory_list:
                try: 
                    del self.inventory_list[self.inventory_list.index(item)]
                except ValueError: 
                    pass
                """if input_val in item['name']:
                    del self.inventory_list[self.inventory_list.index(item)]
                    return 'Successfully deleted'
                else:
                    return 'Item not found in list'"""           
        else:
            return 'There is nothing to delete'
        


    # deletes all items in the list
    def clear_items(self):
        self.inventory_list = []


    # adds the price values for each dict object and displays the total at the 
    # bottom of the list
    def sum_of_items(self):
        total = 0
        for item in self.inventory_list:
            total += float(item['price']) * int(item['quantity'])
        total = round(total, 2)
        return f'\nTotal: ${total}'


    # reads a csv file and returns a list of dictionaries
    def csv_file_reader(self,answ):
        new_list = []
        new_dict_list = []
        with open(answ, newline='') as csvfile:
            invt_reader = csv.reader(csvfile, delimiter=',')
            for row in invt_reader:
                new_list.append(row)
        for i in range(2,len(new_list)):
            new_dict_list.append({
                'name': new_list[i][0],
                'price': new_list[i][1],
                'quantity': new_list[i][2],
            })
        return new_dict_list
    

    def csv_file_writer(self, answ):
        with open(answ, 'w', newline='') as csvfile:
            invt_writer = csv.writer(csvfile, delimiter=',')
            invt_writer.writerow(['Inventory'])
            invt_writer.writerow(['Name'] + ['Price'] + ['Quantity'])
            for item in self.inventory_list:
                invt_writer.writerow([item['name']] + [item['price']] + [item['quantity']])
        print('Exported successfully')


    # exports the dict object to a txt file
    def print_items(self):
        txt_file = open('inventory.txt', 'w')
        txt_file.write('        ---List---\n\n')
        for item in self.inventory_list:
                txt_file.write(item['name'] + ' ' * (10 - len(item['name'])) + '|' + 
                      ' $' + item['price'] + '  |' + 
                      ' ' + item['quantity'] + '  |\n')
        txt_file.write(self.sum_of_items())
        print('printed successfully!\n')
          

if __name__ == '__main__':
    inventory = StoreInventory()
    inventory.start_app()
    #inventory.csv_file_writer()
    print(inventory.inventory_list)




