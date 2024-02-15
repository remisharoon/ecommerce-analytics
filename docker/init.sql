CREATE DATABASE IF NOT EXISTS ecomm;

CREATE USER 'ecomm_data'@'%' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON ecomm.* TO 'ecomm_data'@'%';

GRANT REPLICATION CLIENT ON *.* TO 'ecomm_data'@'%';
FLUSH PRIVILEGES;

