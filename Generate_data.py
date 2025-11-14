import csv
import random
from faker import Faker

fake = Faker()

# 1. Customers
with open("customers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["customer_id", "name", "email"])
    for i in range(1, 51):
        writer.writerow([i, fake.name(), fake.email()])

# 2. Products
with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product_id", "name", "price"])
    for i in range(1, 21):
        writer.writerow([i, fake.word(), random.randint(100, 2000)])

# 3. Orders
with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "customer_id", "order_date"])
    for i in range(1, 60):
        writer.writerow([i, random.randint(1, 50), fake.date()])

# 4. Order Items
with open("order_items.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["item_id", "order_id", "product_id", "quantity"])
    for i in range(1, 150):
        writer.writerow([i, random.randint(1, 59), random.randint(1, 20), random.randint(1, 5)])

# 5. Payments
with open("payments.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["payment_id", "order_id", "amount"])
    for i in range(1, 60):
        writer.writerow([i, i, random.randint(100, 5000)])
