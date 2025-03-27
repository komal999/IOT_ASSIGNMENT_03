import requests
from datetime import datetime, timedelta

# ThingSpeak Configuration
CHANNEL_ID = "2894194"
READ_API_KEY = "DL7V0SU2S9Q3OMU4"


def get_latest_data():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1"
    response = requests.get(url)
    data = response.json()

    if not data.get('feeds'):
        print("\nNo recent data available on ThingSpeak.")
        return

    latest_entry = data['feeds'][0]

    print("\nLatest Sensor Data Received:")
    print(f"Station ID: {latest_entry.get('field4', 'N/A')}")
    print(f"Temperature: {latest_entry['field1']}°C")
    print(f"Humidity: {latest_entry['field2']}%")
    print(f"CO2: {latest_entry['field3']}ppm")
    print(f"Timestamp: {latest_entry['created_at']}")

def get_last_five_hours_data(sensor_type):
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(hours=5)

    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json" \
          f"?api_key={READ_API_KEY}&start={start_date.isoformat()}&end={end_date.isoformat()}"

    response = requests.get(url)
    data = response.json()

    if not data.get('feeds'):
        print("\nNo data available for the last 5 hours!")
        return

    print(f"\nData from the Last 5 Hours for Sensor Type {sensor_type}:")
    for feed in data['feeds']:
        value = feed.get(f'field{sensor_type}', 'N/A')
        print(f"{feed['created_at']} - Value: {value}")

if __name__ == "__main__":
    get_latest_data()
    try:
        sensor_choice = int(input("\nEnter sensor to view (1-Temp, 2-Humidity, 3-CO2): "))
        get_last_five_hours_data(sensor_choice)
    except ValueError:
        print("Invalid input! Please enter a number (1, 2, or 3).")
