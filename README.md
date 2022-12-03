# Store-Inventory
inventory.py

Classes: 

	• StoreInventory
  
Class based Object: 

	• inventory_list : list of dictionaries for each item object
	• Finished : boolean value for while loop in start_app (default is False)
	• command_options : list of strings for each command option that is used is validate_input
  
Methods:

	• start_app: (Takes no parameters) 
  
		○ If self.finished is False, executes create_grid and validate_input
		○ If self.finished is True, executes create_grid method
    
	• validate_input: (Takes no parameters)
  
		○ Takes command input as command 
		○ If command input is in self.command_options, executes command_manager and uses command as an argument 
		○ If command input not in self.command_options, executes a print statement
    
	• command_manager: (Takes 1 parameter as command, arguement passed must be a string
  
		○ depending on the value of command passed into the method, the method will execute another method with the same name as command
		○ The only exception is if “DONE” is passed as an argument, command_manager will then change the value of self.finished = True.
		○ Currently only if the value of command is either “IMPORT” or “EXPORT”, user input is also required and is passed as a variable into the corresponding method.
			§ “IMPORT” will append a csv into the existing self.inventory_list.
      
	• help : (Takes no parameters)  
  
		○ Opens the ‘help.txt’ file as a readable object, then prints the entire text.
    
	• add_item: (Takes no parameters)  
  
		○ Takes name as an input
		○ Creates a boolean checker object and sets it to False
		○ Iterates through self.inventory list
			§ Because each object in self.inventory_list is a dictionary, it will also iterate through each key value in each dictionary
			§ If the there is a key value in a dictionary that matches name, checker will be set to True
		○ If checker is True, a print statement will be called
		○ If checker is False, Takes two input values as price and quantity.
		○ Creates a new Item instance with both inputs as arguments
			§ Appends the value of the create_obj() into self.inventory_list
			§ create_obj returns a dictionary with the values of all inputs collected
      
	• update_item: (Takes no parameters) 
  
		○ Checks if self.inventory_list is empty. If it is, the method will print ‘your list is empty’
		○ If self.inventory_list is not empty, 
			§ Creates a checker variable and sets it to False
			§ Takes three input values as input_val, changed_value_type,new_val
			§ Iterates through each dictionary in self.inventory_list, if there is a key value in the dictionary that matches input_val, then the key value is set to new_val
			§ Checker is set to True
				□ If checker is still False by the end of the method exception, then the method prints ‘Item not found in list’. 
        
	• delete_item: (Takes no parameters)  
  
		○ Checks if self.inventory_list is empty
			§ if list is empty, returns the string 'There is nothing to delete'
		○ If list is not empty, method will collect input as input_val, then iterate through self.inventory_list
			§ if input_val is equal to the 'name' value of the dictionary, method will delete entire dictionary from self.inventoy_list and return 'Successfully deleted'
			§ if input_val does not match the 'name' value of any dictionaries in self.inventory_list, method will return 'Item not found in list' 
      
	• clear_items: (Takes no parameters)  
  
		○ Checks if self.inventory_list is empty:
			§ if list is empty, method will return 'List is already empty'
			§ if list is not empty, method will set value of self.inventory_list to an empty list, and return 'cleared successfully' as a string
      
	• sum_of_items: (Takes no paramters)
  
		○ Creates local intvariable 'total' and sets the value to 0
		○ iterates through each dictionary in self.inventory_list
		○ takes each value from 'price' and 'quantity', and type casts to int and float
			§ calculates the price * quantity and adds the sum to 'total'
			§ rounds 'total' two places passed the decimal point, and returns a string with 'total'
      
	• csv_file_reader: (Takes 1 str parameter as 'answ')
  
		○ Creates two local variables; new_list and new_dict_list. Both are set to empty lists
		○ opens csv file using 'answ' as the destination
			§ takes each row in the csv file and appends a new list to new_list using the items in the csv file
				□ the delimeter is set to ','
			§ creates a dictionary using the values from each list in new_list, and appends the new dictionary to new_dict_list
			§ returns new_dict_list
      
	• csv_file_writer: (Takes 1 str parameter as 'answ')
  
		○ opens an empty csv file using 'answ' as the destination
			§ if a destination does not exist, it will create a new file
		○ writes two lines with descriptions of each object per row
		○ iterates through self.inventory_list and writes a new row to the csv file using the values in each dictionary
		○ after all rows have been added, method will print 'exported successfully'
    
	• print_items: (Takes no parameters')
  
		○ opens a txt file already created.
		○ writes a row containing the list title string
		○ iterates throgh self.inventory_list 
			§ writes a new row using the values of each dictionary with formatting
		○ writes a final row containing the value of self.sum_of_items()
		○ finally, method will print 'printed successfully!'
		
		
		
![image](https://user-images.githubusercontent.com/42852733/205416456-6de61931-c013-4946-b95b-cf2923b2e8fe.png)

