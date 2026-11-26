# 🌤️ Weather CLI – Python Weather Application

## 📌 Project Description

Weather CLI is a command-line weather application developed using Python that allows users to check current weather information by entering a city name.

The application uses the **Open-Meteo Geocoding API** to convert the entered city name into geographical coordinates (latitude and longitude). It then uses the **Open-Meteo Weather API** to retrieve current weather information for that location.

The project demonstrates how Python can interact with external APIs, process JSON responses, and display meaningful information to users through a command-line interface.

## ✨ Features

- Search for weather information using a city name.
- Automatically retrieve geographical coordinates using the Geocoding API.
- Fetch current weather information using the Open-Meteo API.
- Display temperature, humidity, apparent temperature, and wind speed.
- Display weather conditions using weather codes.
- Handle invalid city names and API connection errors.
- Simple and beginner-friendly command-line interface.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **Requests** – For sending HTTP requests to external APIs.
- **Open-Meteo API** – For retrieving geographical and weather information.
- **JSON** – For processing API responses.

## ⚙️ How It Works

The application follows these steps:

1. The user enters a city name.
2. The Geocoding API searches for the city and returns its latitude and longitude.
3. The application extracts the geographical coordinates from the API response.
4. The Weather API uses these coordinates to retrieve current weather information.
5. Python processes the JSON response and extracts the required weather details.
6. The application displays the weather information in the terminal.

## 📂 Project Structure

```text
Weather-CLI/
│
├── weather.py       # Main application
├── README.md        # Project documentation
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Weather-CLI.git
```

### 2. Navigate to the project directory

```bash
cd Weather-CLI
```

### 3. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
venv\Scripts\activate
```

### 5. Install the required dependency

```bash
pip install requests
```

### 6. Run the application

```bash
python weather.py
```

## 📷 Example Usage

```text
================================
       WEATHER APPLICATION
================================

Enter city name: Kathmandu

================================
       WEATHER REPORT
================================

City: Kathmandu
Country: Nepal
Temperature: 22.5 °C
Humidity: 65%
Wind Speed: 8.2 km/h

================================
```

*Note: The displayed values are illustrative examples, not live weather data.*

## 🌐 API References

- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api)
- [Open-Meteo Weather Forecast API](https://open-meteo.com/en/docs)

No API key is required for standard non-commercial use.

## 🎯 Learning Objectives

This project helped me understand and practise:

- Python functions and modular programming.
- Working with dictionaries, lists, and JSON data.
- Making HTTP GET requests using the Requests library.
- Integrating external APIs into Python applications.
- Extracting and processing API responses.
- Exception handling and basic debugging.
- Building a practical command-line application.

## 👨‍💻 Author

**Diken Lamichhane**

Computer Engineering Student

GitHub: Diken537(https://github.com/Diken537)

