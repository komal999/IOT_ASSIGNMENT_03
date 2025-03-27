# IOT_ASSIGNMENT_03


## Project Overview
This project is designed to monitor environmental conditions, specifically tracking temperature, humidity, and CO2 levels. The data is collected through virtual sensors and managed through MQTT to be displayed on ThingSpeak, showcasing real-time data visualization.

## Features
- **Real-time Monitoring**: Continuously track and record temperature, humidity, and CO2 levels.
- **MQTT Integration**: Efficiently manage data transmission using the MQTT protocol.
- **Data Visualization**: Utilize ThingSpeak for real-time data charting and analysis.

## System Architecture
Provide a brief description of the architecture of your system, how components like MQTT, ThingSpeak, and your sensors interact. If possible, include a diagram for clarity.

## Installation Instructions
Detail the steps needed to clone, set up, and run your project:

```bash
git clone https://github.com/komal999/IOT_ASSIGNMENT_03.git
cd iot-environment-monitoring
pip install -r requirements.txt  # Assuming you have a requirements.txt

## Usage

 to run the scripts and what each script does:

python virtual_sensor_data.py  # Runs the virtual sensor simulation
python sensor_data_display.py    # Displays data from ThingSpeak
