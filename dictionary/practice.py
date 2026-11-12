
# Create dictionary with three product and stock number
inventory = {"Laptop": 10, "Mouse": 20, "Keyboard": 15}
print("=> 1 - Inventory:", inventory)
print("--------------------------------------------------------------------------------------")

# Check stock of  product that not exist
print("\n=> 2 - Monitor stock:", inventory.get("Monitor", 0))
("--------------------------------------------------------------------------------------")

# Add two product and change one stock number
inventory.update({"Monitor": 5, "Headphone": 12, "Laptop": 8})
print("\n=> 3 - Updated inventory:", inventory)
("--------------------------------------------------------------------------------------")

# Print every product and its stock
print("\n=> 4 - Products and stock:")
for product, stock in inventory.items():
    print(f"{product}: {stock}")
("--------------------------------------------------------------------------------------")

# Remove sold-out product
inventory["Mouse"] = 0  # Simulate Mouse selling out.
removed_stock = inventory.pop("Mouse")
print("\n=> 5 - Removed Mouse; its stock was:", removed_stock)
print("Inventory after removal:", inventory)
("--------------------------------------------------------------------------------------")

# Add a new product only if it not already exist
inventory.setdefault("Webcam", 7)
print("\n=> 6 - After setdefault:", inventory)
("--------------------------------------------------------------------------------------")

# Total number of item in stock.
total_stock = sum(inventory.values())
print("\n=> 7 - Total items in stock:", total_stock)
("--------------------------------------------------------------------------------------")

# Create backup and clear original dictionary
backup = inventory.copy()
inventory.clear()
print("\n=> 8 - Original inventory:", inventory)
print("Backup inventory:", backup)
