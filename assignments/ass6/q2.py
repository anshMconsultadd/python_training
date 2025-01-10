class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print("Added {} of {}. New stock: {}.".format(quantity, item_name, self.items[item_name]))

    def remove_item(self, item_name, quantity):
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        if self.items[item_name] < quantity:
            print(f"Insufficient stock of {item_name}. Current stock: {self.items[item_name]}.")
            return
        self.items[item_name] -= quantity
        print(f"Removed {quantity} of {item_name}. New stock: {self.items[item_name]}.")

    def query_item(self, item_name):
        if item_name in self.items:
            print(f"Current stock of {item_name}: {self.items[item_name]}.")
            return self.items[item_name]
        else:
            print(f"Item {item_name} not found in inventory.")
            return 0

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item("apple", 10)

    inventory.query_item("apple")
    inventory.remove_item("apple", 3)

    inventory.remove_item("apple", 10) 
      