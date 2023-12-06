import tkinter as tk
import sqlite3


class BlessingDrugShop:
    def __init__(self):
        self.drug_name = ""
        self.price = 0
        self.quantity = 0
        self.total_price = 0

    def calculate_total_price(self):
        self.total_price = self.quantity * self.price

    def submit_data(self):
        self.calculate_total_price()
        print("Drug name:", self.drug_name)
        print("Total price is:", self.total_price)
        self.insert_into_db()

    def insert_into_db(self):
        conn = sqlite3.connect('drug_shop.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS drugs (id INTEGER PRIMARY KEY, drug_name TEXT, price INTEGER, quantity INTEGER, total_price INTEGER)")
        c.execute("INSERT INTO drugs (drug_name, price, quantity, total_price) VALUES (?, ?, ?, ?)",
                  (self.drug_name, self.price, self.quantity, self.total_price))
        conn.commit()
        conn.close()


def submit_form():
    drug_name = drug_name_entry.get()
    price = int(price_entry.get())
    quantity = int(quantity_entry.get())

    H.drug_name = drug_name
    H.price = price
    H.quantity = quantity
    H.submit_data()
    # Update the display after calculation
    total_price_label.config(text=f"Total price is: {H.total_price}")


def display_all_data():
    conn = sqlite3.connect('drug_shop.db')
    c = conn.cursor()
    c.execute("SELECT * FROM drugs")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(row)  # This can be modified to display in the Tkinter window


def validate_input(drug_name):
    return not any(char.isdigit() for char in drug_name)


root = tk.Tk()
root.title("Blessing Drug Shop")

H = BlessingDrugShop()

# Labels
tk.Label(root, text="Enter drug name: ").pack()
validate_drug_name = root.register(validate_input)
drug_name_entry = tk.Entry(root, width=40, validate="key", validatecommand=(validate_drug_name, "%P"))
drug_name_entry.pack()

tk.Label(root, text="Enter Price: ").pack()
price_entry = tk.Entry(root, width=40)  # Adjust width as needed
price_entry.pack()

tk.Label(root, text="Enter Quantity: ").pack()
quantity_entry = tk.Entry(root, width=40)  # Adjust width as needed
quantity_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Display total price
total_price_label = tk.Label(root, text="")
total_price_label.pack()

# Display All Data Button
display_data_button = tk.Button(root, text="Display All Data", command=display_all_data)
display_data_button.pack()

root.mainloop()
