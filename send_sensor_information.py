import paho.mqtt.client as mqtt
import json
import datetime
import argparse

def send_sensor_data(broker_host, broker_port, sensor_id, value):
    """
    Send a single sensor data message to the MQTT broker.
    
    Parameters:
    - broker_host: MQTT broker hostname or IP
    - broker_port: MQTT broker port
    - sensor_id: The ID of the sensor to send data for
    - value: The sensor value to send
    """
    # Create MQTT client
    client = mqtt.Client()
    
    # Connect to the broker
    print(f"Connecting to MQTT broker at {broker_host}:{broker_port}...")
    client.connect(broker_host, broker_port, 60)
    
    # Prepare the topic and payload
    topic = f"planthub/{sensor_id}/sensor_data"
    payload = {
        "value": value,
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    # Convert payload to JSON
    payload_json = json.dumps(payload)
    
    # Publish the message
    print(f"Sending sensor data to topic '{topic}':")
    print(f"Payload: {payload_json}")
    client.publish(topic, payload_json)
    
    # Disconnect
    client.disconnect()
    print("Message sent successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send MQTT sensor data")
    parser.add_argument("--host", default="localhost", help="MQTT broker host")
    parser.add_argument("--port", type=int, default=1883, help="MQTT broker port")
    parser.add_argument("--sensor-id", required=True, help="Sensor ID")
    parser.add_argument("--value", required=True, type=float, help="Sensor value")
    
    args = parser.parse_args()
    
    send_sensor_data(args.host, args.port, args.sensor_id, args.value)