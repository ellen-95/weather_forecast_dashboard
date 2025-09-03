# Weather Forecast Web App

## Purpose
This project provides a simple web application to display weather forecasts for a user-specified location. Users can view temperature trends and sky conditions for up to five days.

## Usage
- Enter a city name in the input field.
- Select the number of forecast days (1-5).
- Choose to view either temperature or sky conditions.
- The app displays a line chart for temperature or images representing sky conditions.

## Demo
![Design Demo](Design_demo.png)

## Deployed Website
Try the app online: [https://ellen-weather-forecast.streamlit.app/](https://ellen-weather-forecast.streamlit.app/)

## How It Works
- The app is built with Streamlit for the frontend interface.
- User input is collected and passed to a backend function.
- The backend fetches weather data from the OpenWeatherMap API.
- Data is processed and visualized using Plotly (for temperature) or images (for sky conditions).
- Error handling is included for invalid city names.

## Tech Stack
- Python: Main programming language.
- Streamlit: For building the interactive web interface.
- Plotly: For data visualization.
- Requests: For making HTTP requests to the weather API.
- python-dotenv: For loading API keys securely from `.env` files.

## Data Source
- OpenWeatherMap API: Provides weather forecast data.

## Setup
1. Clone the repository.
2. install necessary modules
  ```
  pip install streamlit plotly requests python-dotenv
  ```
3.Create a `.env` file with your OpenWeatherMap API key:
  ```
  API_KEY=your_api_key_here
  ```
4. Run the app in the console:
  ```
  streamlit run main.py
  ```
## Further Improvements
- Add support for hourly and weekly forecasts.
- Enhance error handling and user feedback.
- Integrate additional weather metrics (humidity, wind speed, etc.).
- Improve UI/UX design and mobile responsiveness.
- Add localization for multiple languages.

## License
This project is for educational purposes.


