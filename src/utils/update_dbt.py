import yaml
from pathlib import Path

# Define your profile
profile = {
    'ecomm': {
        'target': 'dev',
        'outputs': {
            'dev': {
                'type': 'clickhouse',
                'schema': 'ecommerce',
                'host': 'localhost',
                'user': 'default',
                'password': '',
                'database': 'ecommerce',
                'port': 8124
            }
        }
    }
}

# Write to the profiles.yml file
# Be sure to replace with the path to your dbt directory
dbt_dir = Path.home() / '.dbt'
dbt_dir.mkdir(exist_ok=True)

with open(dbt_dir / 'profiles.yml', 'w') as file:
    documents = yaml.dump(profile, file)
