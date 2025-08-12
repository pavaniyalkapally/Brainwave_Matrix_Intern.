import tkinter as tk
from tkinter import messagebox
import inventory, auth

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")

        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Username").pack()
        self.username = tk.Entry(self.root)
        self.username.pack()
        tk.Label(self.root, text="Password").pack()
        self.password = tk.Entry(self.root, show="*")
        self.password.pack()
        tk.Button(self.root, text="Login", command=self.check_login).pack()

    def check_login(self):
        if auth.login(self.username.get(), self.password.get()):
            self.main_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def main_screen(self):
        self.clear_screen()

        tk.Button(self.root, text="Add Product", command=self.add_product_screen).pack()
        tk.Button(self.root, text="Low Stock Alert", command=self.low_stock_alert).pack()
        tk.Button(self.root, text="Sales Report", command=self.sales_report).pack()

    def add_product_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Product ID").pack()
        pid = tk.Entry(self.root)
        pid.pack()
        tk.Label(self.root, text="Name").pack()
        name = tk.Entry(self.root)
        name.pack()
        tk.Label(self.root, text="Quantity").pack()
        qty = tk.Entry(self.root)
        qty.pack()
        tk.Label(self.root, text="Price").pack()
        price = tk.Entry(self.root)
        price.pack()
        tk.Button(self.root, text="Add", command=lambda: self.save_product(pid.get(), name.get(), qty.get(), price.get())).pack()
        tk.Button(self.root, text="Back", command=self.main_screen).pack()

    def save_product(self, pid, name, qty, price):
        if not pid or not name or not qty.isdigit() or not price.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Invalid input")
            return
        inventory.add_product(pid, name, int(qty), float(price))
        messagebox.showinfo("Success", "Product added successfully")
        self.main_screen()

    def low_stock_alert(self):
        self.clear_screen()
        data = inventory.get_low_stock()
        tk.Label(self.root, text="Low Stock Items:").pack()
        for pid, info in data.items():
            tk.Label(self.root, text=f"{pid}: {info['name']} - Qty: {info['quantity']}").pack()
        tk.Button(self.root, text="Back", command=self.main_screen).pack()

    def sales_report(self):
        self.clear_screen()
        report = inventory.generate_sales_report()
        tk.Label(self.root, text="Sales Report:").pack()
        for pid, total in report.items():
            tk.Label(self.root, text=f"{pid} - Total: ₹{total:.2f}").pack()
        tk.Button(self.root, text="Back", command=self.main_screen).pack()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()