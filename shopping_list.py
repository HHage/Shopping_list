# def shopping_list(grocery_list,):

grocery_list= ["Apples", "Oranges", "Milk", "Strawberries"]
grocery_list.sort() #This Works!
print grocery_list
def add_items(new_item):
	if new_item in grocery_list== True:
		print "This item is already in your list."
	else:
		grocery_list.append(new_item)
		grocery_list.sort()
		print grocery_list



	
	# 	raw_input("What would you like to add to your shopping list?")
	# 		if 

decision=raw_input("Would you like to add an item?")
if decision.lower() == "yes".lower():
	new_item=raw_input("What item would you like to add?")
	add_items(new_item)

	

# print grocery_list



# del grocery_list[2]
# print grocery_list




	