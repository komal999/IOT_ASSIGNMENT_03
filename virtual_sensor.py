import random
import time
import paho.mqtt.client as mqtt

# MQTT credentials
MQTT_BROKER = "mqtt3.thingspeak.com"
MQTT_PORT = 1883
MQTT_USERNAME = "Dy8tOCEcCjQhASQsCw8fBB4"
MQTT_PASSWORD = "AzfjF0bv90sG+c5H/KHeDoOw"
CHANNEL_ID = "2894194"
STATION_ID = "STATION_001"

# callback API version
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=MQTT_USERNAME)

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(" Connected successfully to ThingSpeak MQTT Broker.")
    else:
        print(f" Connection failed with code {reason_code}")

def on_disconnect(client, userdata, flags, reason_code, properties):
    print(f" Unexpected MQTT disconnection. Return code: {reason_code}.")
    time.sleep(5)
    connect_mqtt()

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": random.randint(300, 2000),
        "station_id": STATION_ID,
    }

def connect_mqtt():
    try:
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_start()
        return True
    except Exception as e:
        print(f" Connection error: {e}")
        return False

def publish_data():
    while True:
        if not client.is_connected():
            print("Not connected. Attempting to reconnect...")
            connect_mqtt()
            time.sleep(5)
            continue

        sensor_data = generate_sensor_data()
        topic = f"channels/{CHANNEL_ID}/publish"
        payload = (
            f"field1={sensor_data['temperature']}&"
            f"field2={sensor_data['humidity']}&"
            f"field3={sensor_data['co2']}"
        )

        try:
            client.publish(topic, payload)
            print(f" Published: {sensor_data}")
        except Exception as e:
            print(f"Publish error: {e}")

        time.sleep(60)

if __name__ == "__main__":
    if connect_mqtt():
        try:
            publish_data()
        except KeyboardInterrupt:
            print("\nShutting down...")
        finally:
            client.loop_stop()
            client.disconnect()
    else:
        print(" Failed to establish initial connection")
