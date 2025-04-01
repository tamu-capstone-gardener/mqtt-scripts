# `send_sensor_information.py`

A utility script that sends sensor data to a Planthub MQTT broker. This script allows you to easily publish sensor readings to the Planthub system for testing and integration purposes.

## Features

- Sends sensor readings to a specified MQTT broker
- Automatically formats the data with the current timestamp
- Uses the Planthub topic structure (`planthub/{sensor_id}/sensor_data`)
- Command-line interface for easy use

## Requirements

- Python 3
- paho-mqtt library (install with `pip install paho-mqtt`)

## Usage

```bash
python send_sensor_information.py --sensor-id <SENSOR_ID> --value <SENSOR_VALUE> [--host <BROKER_HOST>] [--port <BROKER_PORT>]
```

## Parameters

- `--sensor-id`: The unique identifier for the sensor (required)
- `--value`: The sensor reading value (required, must be a number)
- `--host`: MQTT broker hostname or IP address (default: "localhost")
- `--port`: MQTT broker port number (default: 1883)

## Example

Send a moisture sensor reading of 42.5 to a local MQTT broker:

```bash
python send_sensor_information.py --sensor-id moisture_sensor_01 --value 42.5
```

Send a temperature reading to a remote broker:

```bash
python send_sensor_information.py --sensor-id temp_sensor_02 --value 23.8 --host mqtt.planthub.example.com --port 1883
```

## Message Format

The script sends messages in JSON format with the following structure:

```json
{
  "value": <sensor_value>,
  "timestamp": "<ISO-format timestamp>"
}
```

Messages are published to the topic: `planthub/{sensor_id}/sensor_data`