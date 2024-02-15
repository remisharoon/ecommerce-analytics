from sqlalchemy import Table, MetaData, Column, Integer, String, Float, Date, ForeignKey, create_engine

# Define the connection string
mysql_conn_string = 'mysql+mysqlconnector://ecomm_data:password@mysql-ea:3306/ecomm'
# clickhouse_conn_string = 'clickhouse+native://default:@localhost:8124/default'

# Create an engine that connects to the database using the connection string
mysql_engine = create_engine(mysql_conn_string)
# clickhouse_engine = create_engine(clickhouse_conn_string)

# Initialize metadata object
metadata = MetaData()

# Define the tables
products = Table(
    'products', metadata,
    Column('id', Integer, primary_key=True),
    Column('product_name', String(255)),
    Column('product_description', String(255)),
    Column('product_price', Float)
)

customers = Table(
    'customers', metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(255)),
    Column('last_name', String(255)),
    Column('email', String(255)),
    Column('address', String(255))
)

orders = Table(
    'orders', metadata,
    Column('id', Integer, primary_key=True),
    Column('customer_id', Integer, ForeignKey('customers.id')),
    Column('order_date', Date),
    Column('total_amount', Float)
)

order_items = Table(
    'order_items', metadata,
    Column('id', Integer, primary_key=True),
    Column('order_id', Integer, ForeignKey('orders.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('quantity', Integer),
    Column('price', Float)
)

# Create all tables in the metadata
metadata.create_all(mysql_engine)
# metadata.create_all(clickhouse_engine)
