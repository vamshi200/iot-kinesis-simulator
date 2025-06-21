import json
import time
import random
from datetime import datetime

def generate_sensor_data():
    return {
        "sensor_id": f"SENSOR-{random.randint(1, 5)}",
        "temperature": round(random.uniform(20.0, 40.0), 2),
        "humidity": random.randint(30, 80),
        "timestamp": datetime.utcnow().isoformat()
    }

# Loop forever and print one reading every 2 seconds
while True:
    data = generate_sensor_data()
    print(json.dumps(data))  # <- This is what shows up in your terminal
    time.sleep(2)
