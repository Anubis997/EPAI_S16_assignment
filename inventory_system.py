import copy

# Function to create an initial inventory
def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    inventory = {
        'Electronics': {
            'Laptop': {'name': 'Laptop', 'price': 1200, 'quantity': 10},
            'smartphone': {'name': 'Smartphone', 'price': 800, 'quantity': 50}
        },
        'Groceries': dict([
            ('apple', {'name': 'Apple', 'price': 1, 'quantity': 200}),
            ('banana', {'name': 'Banana', 'price': 0.5, 'quantity': 150})
        ])
    }
    return inventory

# Function to update an item in the inventory
def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    if category in inventory and item_name in inventory[category]:
        inventory[category][item_name].update(update_info)
    else:
        print(f"Category '{category}' or item '{item_name}' not found in inventory.")

# Function to merge two inventories
def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    for category, items in inv2.items():
        if category not in inv1:
            inv1[category] = items
        else:
            for item, details in items.items():
                if item in inv1[category]:
                    # Merge item details, e.g., summing quantities
                    inv1[category][item]['quantity'] += details.get('quantity', 0)
                else:
                    inv1[category][item] = details
    return inv1

# Function to retrieve all items in a category
def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    return inventory.get(category, {})

# Function to find the most expensive item in the inventory
def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    max_price = -1
    most_expensive = None
    for category, items in inventory.items():
        for item_name, details in items.items():
            if details['price'] > max_price:
                max_price = details['price']
                most_expensive = details
    return most_expensive

# Function to check if an item is in stock
def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for category, items in inventory.items():
        if item_name in items:
            return items[item_name] if items[item_name]['quantity'] > 0 else None
    return None

# Function to view available categories
def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return list(inventory.keys())

# Function to view all items
def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    all_items = []
    for items in inventory.values():
        all_items.extend(items.values())
    return all_items

# Function to view category-item pairs
def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    return [(category, list(items.keys())) for category, items in inventory.items()]

# Function to copy inventory
def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    return copy.deepcopy(inventory) if deep else copy.copy(inventory)
