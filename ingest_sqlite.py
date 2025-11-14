import sqlite3
import csv

# Connect to the database (creates ecom.db if not exists)
conn = sqlite3.connect("ecom.db")
cur = conn.cursor()

# 1. Create tables
cur.execute("DROP TABLE IF EXISTS customers")
cur.execute("DROP TABLE IF EXISTS products")
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS order_items")
cur.execute("DROP TABLE IF EXISTS payments")

cur.execute("""
CREATE TABLE customers(
    customer_id INTEGER,
    name TEXT,
    email TEXT
)
""")

cur.execute("""
CREATE TABLE products(
    product_id INTEGER,
    name TEXT,
    price INTEGER
)
""")

cur.execute("""
CREATE TABLE orders(
    order_id INTEGER,
    customer_id INTEGER,
    order_date TEXT
)
""")

cur.execute("""
CREATE TABLE order_items(
    item_id INTEGER,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER
)
""")

cur.execute("""
CREATE TABLE payments(
    payment_id INTEGER,
    order_id INTEGER,
    amount INTEGER
)
""")

# 2. Helper function to load CSV files into tables
def load_csv(file, table):
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            placeholders = ",".join("?" * len(row))
            cur.execute(f"INSERT INTO {table} VALUES ({placeholders})", row)

# 3. Load all CSV files
load_csv("customers.csv", "customers")
load_csv("products.csv", "products")
load_csv("orders.csv", "orders")
load_csv("order_items.csv", "order_items")
load_csv("payments.csv", "payments")

# 4. Save and close
conn.commit()
conn.close()

print("Data successfully inserted into ecom.db!")
