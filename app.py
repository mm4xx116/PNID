def calculate_total_value(items):
    return sum(item['price'] * item['quantity'] for item in items)

if __name__ == "__main__":
    inventory = [{"name": "Laptop", "price": 1000, "quantity": 5}]
    print(f"Total: {calculate_total_value(inventory)}")