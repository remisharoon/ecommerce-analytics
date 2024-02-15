
# E-Commerce Analytics Demo Project

## Overview

This open-source E-Commerce Analytics Demo Project showcases a powerful, integrated analytics solution tailored for e-commerce platforms. Utilizing cutting-edge technologies such as Apache Kafka, Zookeeper, ClickHouse, MySQL, and Metabase, the project offers a comprehensive environment for real-time data processing and analytics visualization. Ideal for data scientists, application developers, and e-commerce business owners, this demo project provides insightful analytics on consumer behavior, sales performance, and operational efficiency.

## Features

- **Real-Time Data Streaming and Processing**: Leverages Apache Kafka and Zookeeper for efficient data ingestion and streaming.
- **Advanced Data Storage**: Uses ClickHouse for analytical processing and MySQL for transactional data storage.
- **Interactive Dashboards and Analytics**: Employs Metabase for creating dynamic dashboards and visualizing data analytics.
- **Custom Data Generation**: Features a custom data generator for simulating e-commerce transactions and events.
- **Scalable Architecture**: Designed to scale horizontally to accommodate more Kafka brokers or database instances as needed.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- A basic understanding of containerization and microservices.

### Installation

1. **Clone the Repository**

   ```
   git clone https://github.com/remisharoon/ecommerce-analytics.git
   cd ecommerce-analytics
   ```

2. **Build and Run the Services**

   Use Docker Compose to build and start the services:

   ```
   docker-compose up -d
   ```

3. **Access the Metabase Dashboard**

   Open your browser and navigate to `http://localhost:3002` to access Metabase and explore the analytics dashboards.

4. **Generate Sample Data**

   Execute the data generator service to populate your environment with e-commerce transaction data.

### Configuration

Detailed instructions on configuring each service (Kafka, Zookeeper, ClickHouse, MySQL, Metabase) are provided in the respective sections below.

## Services Configuration

### Kafka and Zookeeper

- **Kafka**: Configured for real-time data streaming with support for multiple brokers.
- **Zookeeper**: Manages Kafka's cluster coordination and configuration.

### ClickHouse

- **ClickHouse**: Optimized for fast analytical queries, ideal for time-series data.

### MySQL

- **MySQL**: Stores transactional data and user information, configured with initial schema and data setup.

### Metabase

- **Metabase**: Provides interactive data visualization and analytics tools.

## Contributing

We welcome contributions from the community! Whether you're interested in fixing bugs, adding new features, or improving documentation, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Support

If you need help or have any questions, please open an issue in the project's GitHub issue tracker.
