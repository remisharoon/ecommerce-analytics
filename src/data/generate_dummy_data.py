from faker import Faker
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import insert
from sqlalchemy.orm import sessionmaker
from src.models.relational import products, customers, orders, order_items, mysql_engine, metadata
import src.models.ecommerce
import time

# Set up Faker
fake = Faker()

# Create a Session
Session = sessionmaker(bind=mysql_engine)
session = Session()

# Generate data for 'products' table and save the IDs
product_ids = []
for _ in range(100000):
    product = products.insert().values(product_name=fake.name(), product_description=fake.text(), product_price=fake.random_int(min=1, max=10000, step=1))
    result = session.execute(product)
    product_ids.append(result.inserted_primary_key[0])

# Generate data for 'customers' table and save the IDs
customer_ids = []
for _ in range(100000):
    customer = customers.insert().values(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), address=fake.address())
    result = session.execute(customer)
    customer_ids.append(result.inserted_primary_key[0])

# Generate data for 'orders' and 'order_items' tables continuously
while True:
    # Randomly select a customer
    customer_id = fake.random_element(customer_ids)

    # Create a new order for the customer
    order = orders.insert().values(
        customer_id=customer_id,
        order_date=fake.date(),
        total_amount=fake.random_int(min=1, max=10000, step=1)
    )
    result = session.execute(order)
    order_id = result.inserted_primary_key[0]

    # Create order items for the order
    for _ in range(fake.random_int(min=1, max=10)):  # Random number of items per order
        order_item = order_items.insert().values(
            order_id=order_id,
            product_id=fake.random_element(product_ids),
            quantity=fake.random_int(min=1, max=10, step=1),
            price=fake.random_int(min=1, max=1000, step=1)
        )
        session.execute(order_item)

    # Commit the transaction
    session.commit()

    # Wait for a certain period before creating the next order
    time.sleep(fake.random_int(min=1, max=10))  # Wait for 1 to 10 seconds





