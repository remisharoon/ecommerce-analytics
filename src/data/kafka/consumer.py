from kafka import KafkaConsumer
from datetime import datetime
from src.connections.ch_conn import ch_client
import json

# Kafka topics to subscribe
topics = ["products", "customers", "orders", "order_items"]

# Set up Kafka consumer
consumer = KafkaConsumer(
    *topics,
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    # Get the message value (our data)
    data = message.value
    print(data)
    event = data.get('type', None)
    # Extract row values
    row_values = data.get('row', {}).get('values', {})
    version = data.get('version', 1)
    deleted = 0

    if event == "DeleteRowsEvent":
        deleted = 1
    elif event == "UpdateRowsEvent":
        version += 1

    # Insert or update data into ClickHouse
    try:
        if message.topic == "products":
            data = [[row_values['id'], row_values['product_name'], row_values['product_description'], row_values['product_price'], version, deleted]]
            ch_client.insert('products', data, column_names=['id', 'product_name', 'product_description', 'product_price', '_version', 'deleted'], database='ecommerce')
        elif message.topic == "customers":
            data = [[row_values['id'], row_values['first_name'], row_values['last_name'], row_values['email'], row_values['address'], version, deleted]]
            ch_client.insert('customers', data, column_names=['id', 'first_name', 'last_name', 'email', 'address', '_version', 'deleted'], database='ecommerce')
        elif message.topic == "orders":
            order_date = datetime.strptime(row_values['order_date'], "%Y-%m-%d").date()  # Convert string to date
            data = [[row_values['id'], row_values['customer_id'], order_date, row_values['total_amount'], version, deleted]]
            ch_client.insert('orders', data, column_names=['id', 'customer_id', 'order_date', 'total_amount', '_version', 'deleted'], database='ecommerce')
        elif message.topic == "order_items":
            data = [[row_values['id'], row_values['order_id'], row_values['product_id'], row_values['quantity'], row_values['price'], version, deleted]]
            ch_client.insert('order_items', data, column_names=['id', 'order_id', 'product_id', 'quantity', 'price', '_version', 'deleted'], database='ecommerce')
    except Exception as e:
        print(f"Failed to write data to ClickHouse: {e}")
