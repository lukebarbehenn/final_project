# INST326 Final Project

import requests

class weather():

    def getweather(lat, lon):
        """Scrapes the web for current weather info"""

        api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8c6d96932235d74117595f9e8423547b'

        request = requests.get(api_url)

        x = request.json()

        temperature = x['main']['temp']
        fahrenheit = (temperature - 273.15) * 1.8 + 32
        
        feelslike = x['main']['feels_like']
        fahrenheit_fl = (feelslike - 273.15) * 1.8 + 32

        humidity = x['main']['humidity']

        main_weather = x['weather'][0]['description']

        ret_val = f'Weather: {main_weather} \nCurrent Temperature: {fahrenheit} \nFeels Like: {fahrenheit_fl} \nHumidity: {humidity}'

        return ret_val
    
    def analyze_weather(temp, humidity):
        """Provides an analysis about the weather"""
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

    def recommend(temp, weather):
        """Makes recommendations or predictions to the user based on weather """
        if "rain" or "drizzle" in weather:
            return "It's going to rain; don't forget to carry an umbrella!"
        if temp < 32:
            return "It's very cold; make sure to wear heavy winter clothes."
        if temp > 90:
            return "It's very hot; stay hydrated and avoid going out during peak hours."
        else: 
            return "Weather looks nice; you should be good!"

def user_weather():

    """User interaction with weather data """

    dc_lat = 38.91982068626991
    dc_lon = -77.03656476393802

    arl_lat = 38.8869342864727
    arl_lon = -77.12104283496652

    alx_lat = 38.81738004650533
    alx_lon = -77.10816225921265

    bsd_lat = 38.9755976253306
    bsd_lon = -77.11377134028886

    cp_lat = 39.00539708606798
    cp_lon = -76.92506200115137
   
    user_input = input("Enter a state. DC, MD, or VA: ").upper()

    if user_input == "DC":
        result = weather.getweather(dc_lat, dc_lon)
        print(result)

    elif user_input == "VA":
        va_state_input = input("Enter a City. Arlington or Alexandria: ").lower()
        if va_state_input == "arlington":
            result = weather.getweather(arl_lat, arl_lon)
            print(result)
        if va_state_input == "alexandria":
            result = weather.getweather(alx_lat, alx_lon)
            print(result)

    elif user_input == "MD": 
        md_state_input = input("Enter a City. Bethesda or College Park: ").lower()
        if md_state_input == "bethesda":
            result = weather.getweather(bsd_lat, bsd_lon)
            print(result)
        if md_state_input == "college park":
            result = weather.getweather(cp_lat, cp_lon)
            print(result)
    else: 
        print("Invalid State!")

def user_analysis():
    """User interaction with analysis and reccomendation system """

    temp = int(input("Enter temperature: "))
    humidity = int(input("Enter humidity: "))
    cur_weather = input("Enter current weather: ")

    result = weather.analyze_weather(temp, humidity)
    result2 = weather.recommend(temp, cur_weather)
    print(result)
    print(result2)

if __name__ == "__main__":
    user_weather()
    user_analysis()

    
