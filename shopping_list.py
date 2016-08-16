# def shopping_list(grocery_list,):

grocery_list= ["Apples", "Oranges", "Milk", "Strawberries"]
grocery_list.sort() #This Works!
print "Welcome, your items are", grocery_list

def add_items(new_item):
	while(True):
		print "Type exit to exit"
		print "your items are", grocery_list
		# new_item= raw_input("What item would you like to add? ")
		if (new_item=="exit"):
			break
		elif new_item in grocery_list== True:
			print "This item is already in your list."
		else:
			grocery_list.append(new_item)
			grocery_list.sort()
			print grocery_list
			
def del_item(remove_item):
	if  remove_item in grocery_list == True:
			grocery_list.remove(remove_item)
			grocery_list.sort()
			print grocery_list.sort()
	else:
		print "This item is not on your list."
		grocery_list.sort()
		print grocery_list





	
	# 	raw_input("What would you like to add to your shopping list?")
	# 		if 

decision=raw_input("Would you like to add an item? ")
if decision.lower() == "yes".lower():
	new_item=raw_input("What item would you like to add? ")
	add_items(new_item)

remove_decision=raw_input("Would you like to remove an item? ")
if remove_decision.lower()== "yes".lower():
	remove_item=raw_input("What item would you like to remove? ")
	del_item(remove_decision)

	

# print grocery_list



# del grocery_list[2]
# print grocery_list

# elif line 14 being glossed over

#line 23-26 not are being glosses over to else statement
#line 




	