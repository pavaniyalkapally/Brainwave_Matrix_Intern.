import json

DB_FILE = "database.json"

def load_inventory():
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_inventory(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_product(pid, name, qty, price):
    data = load_inventory()
    data[pid] = {"name": name, "quantity": qty, "price": price}
    save_inventory(data)

def edit_product(pid, name, qty, price):
    data = load_inventory()
    if pid in data:
        data[pid] = {"name": name, "quantity": qty, "price": price}
        save_inventory(data)

def delete_product(pid):
    data = load_inventory()
    if pid in data:
        del data[pid]
        save_inventory(data)

def get_low_stock(threshold=5):
    data = load_inventory()
    return {pid: info for pid, info in data.items() if info["quantity"] <= threshold}

def generate_sales_report():
    data = load_inventory()
    return {pid: info["quantity"] * info["price"] for pid, info in data.items()}