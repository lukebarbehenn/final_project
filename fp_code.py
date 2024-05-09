# INST326 0204 Group 8 Final Project - Weather Analysis 
# Authors: Luke Barbehenn and Don Nguyen 

import requests

class Weather:
    """A class for fetching and analyzing weather data from the OpenWeather API."""

    @staticmethod
    def get_weather(lat, lon):
        """
        Fetches the current weather information for a given latitude and longitude.

        Args:
            lat (float): The latitude of the location.
            lon (float): The longitude of the location.

        Returns:
            str: A formatted string containing weather description, current temperature,
                 'feels like' temperature, and humidity.
        """
        api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8c6d96932235d74117595f9e8423547b'

        request = requests.get(api_url)
        x = request.json()

        temperature = x['main']['temp']
        fahrenheit = (temperature - 273.15) * 1.8 + 32
        
        feelslike = x['main']['feels_like']
        fahrenheit_fl = (feelslike - 273.15) * 1.8 + 32

        humidity = x['main']['humidity']
        main_weather = x['weather'][0]['description']

        return f'Weather: {main_weather} \nCurrent Temperature: {fahrenheit} \nFeels Like: {fahrenheit_fl} \nHumidity: {humidity}'
    
    @staticmethod
    def analyze_weather(temp, humidity):
        """
        Provides an analysis of the weather based on temperature and humidity.

        Args:
            temp (float): Current temperature in degrees Fahrenheit.
            humidity (int): Current humidity as a percentage.

        Returns:
            str: A description of the current weather based on the given parameters.
        """
        analysis = "Weather is "
        if temp > 90:
            analysis += "very hot"
        elif temp > 70:
            analysis += "moderately hot"
        elif temp > 50:
            analysis += "mild"
        elif temp > 32:
            analysis += "cold"
        else:
            analysis += "very cold"

        if humidity > 80:
            analysis += " and highly humid."
        elif humidity > 50:
            analysis += " and moderately humid."
        else:
            analysis += " and dry."

        return analysis

    @staticmethod
    def recommend(temp, weather):
        """
        Provides recommendations based on current temperature and weather conditions.

        Args:
            temp (float): Current temperature in degrees Fahrenheit.
            weather (str): Descriptive string of current weather conditions.

        Returns:
            str: Recommendation based on the current weather.
        """
        if "rain" in weather or "drizzle" in weather or "mist" in weather:
            return "It's going to rain; don't forget to carry an umbrella!"
        if temp < 32:
            return "It's very cold; make sure to wear heavy winter clothes."
        if temp > 90:
            return "It's very hot; stay hydrated and avoid going out during peak hours."
        return "Weather looks nice; you should be good!"

def user_weather():
    """
    Main function for user interaction with weather data.

    Allows the user to select a state and city to fetch weather information for that location.
    """
    # Latitude and longitude for DC and surrounding areas in MD and VA
    dc_lat, dc_lon = 38.91982068626991, -77.03656476393802
    arl_lat, arl_lon = 38.8869342864727, -77.12104283496652
    alx_lat, alx_lon = 38.81738004650533, -77.10816225921265
    bsd_lat, bsd_lon = 38.9755976253306, -77.11377134028886
    cp_lat, cp_lon = 39.00539708606798, -76.92506200115137
   
    user_input = input("Enter a state. DC, MD, or VA: ").upper()

    if user_input == "DC":
        result = Weather.get_weather(dc_lat, dc_lon)
        print(result)
    elif user_input == "VA":
        va_state_input = input("Enter a City. Arlington or Alexandria: ").lower()
        if va_state_input == "arlington":
            result = Weather.get_weather(arl_lat, arl_lon)
            print(result)
        elif va_state_input == "alexandria":
            result = Weather.get_weather(alx_lat, alx_lon)
            print(result)
        else:
            print("Invalid City!")
            exit()
    elif user_input == "MD":
        md_state_input = input("Enter a City. Bethesda or College Park: ").lower()
        if md_state_input == "bethesda":
            result = Weather.get_weather(bsd_lat, bsd_lon)
            print(result)
        elif md_state_input == "college park":
            result = Weather.get_weather(cp_lat, cp_lon)
            print(result)
        else:
            print("Invalid City!")
            exit()
    else:
        print("Invalid State!")
        exit()

def user_analysis():
    """
    User interaction function for receiving analysis and recommendations based on input weather conditions.

    Prompts user for temperature, humidity, and current weather, then provides analysis and recommendations.
    """
    temp = float(input("Enter temperature: "))
    humidity = int(input("Enter humidity: "))
    cur_weather = input("Enter current weather: ")

    result = Weather.analyze_weather(temp, humidity)
    result2 = Weather.recommend(temp, cur_weather)
    print("Analysis: " + result)
    print("Recomendation: " + result2)

if __name__ == "__main__":
    user_weather()
    user_analysis()
