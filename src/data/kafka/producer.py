import json
import datetime
from confluent_kafka import Producer
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent

# Set up Kafka producer
p = Producer({'bootstrap.servers': 'localhost:9092'})

# Define a delivery report function to handle delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

mysql_settings = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'passwd': 'password'}

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

stream = BinLogStreamReader(
    connection_settings=mysql_settings,
    server_id=100,  # Unique ID for the slave (this script)
    blocking=True,
    only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent],
    only_schemas=['ecomm'],  # Only listen to changes in the 'ecomm' DB
)

try:
    for binlogevent in stream:
        for row in binlogevent.rows:
            event = {"schema": binlogevent.schema, "table": binlogevent.table, "type": type(binlogevent).__name__, "row": row}
            print(event)
            # Convert the event to a JSON string
            event_json = json.dumps(event, cls=DateTimeEncoder)

            # Send the event to the appropriate Kafka topic
            try:
                p.produce(binlogevent.table, event_json, callback=delivery_report)
            except BufferError:
                print('Buffer error, waiting for queue to drain')
                p.flush()
            except Exception as e:
                print(f'Failed to deliver message: {e}')

    # Wait for any outstanding messages to be delivered
    p.flush()

except KeyboardInterrupt:
    print("Stopping...")

finally:
    stream.close()
