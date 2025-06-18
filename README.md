# Weather Data Collector

A Python script to fetch and compile daily weather data for major Indian cities using the OpenWeather API. Designed for automation and easy integration with scheduling tools.

## Features

- Retrieves current weather data including temperature, humidity, pressure, and wind speed
- Supports multiple cities in India
- Outputs data as a CSV file for easy analysis
- Easy to schedule for automated runs using tools like Windows Task Scheduler

## Setup

**Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   
******Install required Python packages:******

bash
pip install -r requirements.txt
Obtain an API key from OpenWeather.

**Update the script:**

Replace the placeholder "replace your api key" with your actual OpenWeather API key in the script, or

Use environment variables for better security (optional).

Usage
Run the script manually:

bash
python hey.py
The script will fetch weather data and save it to weather_data.csv.

Scheduling (Optional)
Set up Windows Task Scheduler or any other scheduler to run the script automatically at desired intervals.

Notes
Do NOT share your API key publicly.

The current version uses a placeholder API key string; replace it with your own before running.
