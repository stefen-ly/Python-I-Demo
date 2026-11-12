
# Create item list contain 5 items. With "milk" twice
shopping_list = ["milk", "rice", "apple", "milk", "sugar"]
print("=> 1 - Shopping list:", shopping_list)
("--------------------------------------------------------------------------------------")

# Print the second item,(last item, and total item)
print("\n=> 2")
print("Second item:", shopping_list[1])
print("Last item:", shopping_list[-1])
print("Total items:", len(shopping_list))
("--------------------------------------------------------------------------------------")

# Add egg to the end and insert bread as the second
shopping_list.append("eggs")
shopping_list.insert(1, "bread")
print("\n=> 3 - After adding eggs and bread:", shopping_list)
("--------------------------------------------------------------------------------------")

# Remove milk once
shopping_list.remove("milk")
print("\n=> 4 - After removing milk once:", shopping_list)
("--------------------------------------------------------------------------------------")

# Check if milk still exist and count item
print("\n=> 5")
print("Milk still exists:", "milk" in shopping_list)
print("Remaining items:", len(shopping_list)) 
("--------------------------------------------------------------------------------------")

# Print every item and total.
print("\n=> 6 - Shopping items:")
for item in shopping_list:
    print(item)
print("Total items:", len(shopping_list))
("--------------------------------------------------------------------------------------")

# Remove last item (print it and the list)
removed_item = shopping_list.pop()
print("\n=> 8 - Removed last item:", removed_item)
print("Updated list:", shopping_list)
("--------------------------------------------------------------------------------------")

# Sort alphabetically, preserving the separate unsort copy
unsorted_list = shopping_list.copy()
shopping_list.sort()
print("\n=> 9 - Sorted list:", shopping_list)
print("Unsorted copy:", unsorted_list)
