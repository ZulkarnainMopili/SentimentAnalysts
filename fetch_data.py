import requests
import json

def fetch_data(api_url, params=None, headers=None):
    try:
        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def save_data_to_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {file_path}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

def main():
    api_url = "https://api.open-meteo.com/v1/forecast"  # Example API endpoint
    params = {
        'latitude': 35.6895,
        'longitude': 139.6917,
        'hourly': 'temperature_2m'
    }
    headers = {
        'Content-Type': 'application/json'
    }

    data = fetch_data(api_url, params, headers)
    if data:
        save_data_to_file(data, "weather_data.json")

if __name__ == "__main__":
    main()

