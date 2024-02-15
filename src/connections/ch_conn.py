import clickhouse_connect

ch_client = clickhouse_connect.get_client(host='localhost', port=8124, database='ecommerce')