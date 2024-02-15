# from src.connections.ch_conn import ch_client as client


def execute_sql_file(file_path):
    with open(file_path, 'r') as file:
        sql_commands = file.read().split(';')
        for command in sql_commands:
            try:
                client.command(command)
            except Exception as e:
                print(f"Failed to execute command: {e}")


if __name__ == '__main__':
    execute_sql_file('ecommerce_setup.sql')
