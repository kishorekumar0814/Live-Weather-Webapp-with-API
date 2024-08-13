# Live-Weather-Webapp-with-API

## Overview
This is a simple weather web application developed using Python Flask, HTML, and CSS. The application allows users to input a city name and get the current weather information, including temperature, weather description, and other relevant data.

## Features
- Fetches current weather data from OpenWeatherMap API.
- Displays weather information including temperature, humidity, and weather description.
- Responsive design with a modern, glassmorphic interface.
- Background image of a dynamic GIF for visual appeal.

## Technologies
- **Backend**: Python Flask
- **Frontend**: HTML, CSS
- **API**: OpenWeatherMap

## Setup

### Prerequisites
- Python 3.x
- Flask
- Requests library

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kishorekumar0814/Live-Weather-Webapp-with-API.git
    ```
2. Navigate to the project directory:
    ```bash
    cd weather-web-app
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `.env` file in the root directory and add your OpenWeatherMap API key:
    ```
    API_KEY=your_openweathermap_api_key
    ```
5. Run the Flask application:
    ```bash
    python app.py
    ```

6. Open your web browser and navigate to `http://127.0.0.1:5000` to view the application.

## Project Structure
- `app.py`: Main Flask application file.
- `templates/`: Contains HTML files.
  - `index.html`: The main page template.
- `static/`: Contains static files like CSS.
  - `styles.css`: CSS file for styling.
- `requirements.txt`: List of Python packages required for the project.

## API Key
Replace `'your_openweathermap_api_key'` in the `.env` file with your actual API key from OpenWeatherMap.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or issues, please contact [Mail](mailto:kishorekumar1409@gmail.com).
