# Weather Information Application

## Overview

A Python-based weather application that retrieves real-time weather information using Open-Meteo APIs.

The application accepts a city name from the user, converts it into geographical coordinates through a geocoding API, and then fetches current weather data including temperature, humidity, wind speed, and weather conditions.

## Features

* Search weather by city name
* Real-time weather information
* Temperature display
* Humidity display
* Wind speed display
* Weather condition display
* Invalid city validation
* Modular code structure using functions

## Technologies Used

* Python
* Requests Library
* Open-Meteo Geocoding API
* Open-Meteo Weather API

## Project Structure

* `get_coordinates()` - Retrieves latitude and longitude from city name
* `get_weather()` - Fetches weather data using coordinates
* `display_weather()` - Displays formatted weather information
* `main()` - Controls application flow

## Learning Outcomes

* API Integration
* JSON Parsing
* HTTP Requests
* Python Functions
* Dictionary Handling
* Input Validation
* Error Handling Concepts
