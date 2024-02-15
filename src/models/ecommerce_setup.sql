CREATE DATABASE IF NOT EXISTS ecommerce;

CREATE TABLE IF NOT EXISTS ecommerce.products (
    id Int32,
    product_name String,
    product_description String,
    product_price Float64,
    _version UInt64,
    deleted UInt8 DEFAULT 0
) ENGINE = ReplacingMergeTree(_version)
ORDER BY id;

CREATE TABLE IF NOT EXISTS ecommerce.customers (
    id Int32,
    first_name String,
    last_name String,
    email String,
    address String,
    _version UInt64,
    deleted UInt8 DEFAULT 0
) ENGINE = ReplacingMergeTree(_version)
ORDER BY id;

CREATE TABLE IF NOT EXISTS ecommerce.orders (
    id Int32,
    customer_id Int32,
    order_date Date,
    total_amount Float64,
    _version UInt64,
    deleted UInt8 DEFAULT 0
) ENGINE = ReplacingMergeTree(_version)
ORDER BY id;

CREATE TABLE IF NOT EXISTS ecommerce.order_items (
    id Int32,
    order_id Int32,
    product_id Int32,
    quantity Int32,
    price Float64,
    _version UInt64,
    deleted UInt8 DEFAULT 0
) ENGINE = ReplacingMergeTree(_version)
ORDER BY id;
