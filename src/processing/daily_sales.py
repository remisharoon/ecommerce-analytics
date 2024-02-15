from src.connections.ch_conn import ch_client

# Create daily_sales table in ClickHouse
ch_client.command('''
    CREATE TABLE IF NOT EXISTS ecommerce.daily_sales (
        date Date,
        sales Float64
    ) ENGINE = MergeTree()
    ORDER BY date
''')


# Perform the denormalization and aggregation within ClickHouse
query = """
    INSERT INTO ecommerce.daily_sales (date, sales)
    SELECT
        orders.order_date AS date,
        SUM(order_items.price * order_items.quantity) AS sales
    FROM
        ecommerce.orders AS orders
    JOIN 
        ecommerce.order_items AS order_items ON orders.id = order_items.order_id
    GROUP BY 
        orders.order_date;
"""

ch_client.command(query)
