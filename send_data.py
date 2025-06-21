import boto3
import json
import time
import random
from datetime import datetime

firehose = boto3.client('firehose', region_name='us-east-1')  # Change region if needed

def generate_sensor_data():
    return {
        "sensor_id": f"SENSOR-{random.randint(1, 5)}",
        "temperature": round(random.uniform(20.0, 40.0), 2),
        "humidity": random.randint(30, 80),
        "timestamp": datetime.utcnow().isoformat()
    }

while True:
    data = generate_sensor_data()
    print(f"Sending: {data}")

    firehose.put_record(
        DeliveryStreamName='iot-sensor-firehose',  # Your Firehose stream name
        Record={
            'Data': json.dumps(data) + "\n"  # Firehose needs newline-delimited records
        }
    )

    time.sleep(2)
