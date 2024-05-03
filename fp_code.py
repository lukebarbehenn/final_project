# INST326 Final Project 

from bs4 import BeautifulSoup
import requests

def main():
    # Prompt the user to enter a state
    state = input("Enter a state (DC, VA, or MD): ").upper()
    
    # Define cities for each state
    cities = {
        'DC': ['Washington'],
        'VA': ['Arlington', 'Fairfax', 'Alexandria'],
        'MD': ['Rockville', 'Bethesda', 'College Park']
    }
    
    # Check if the entered state is valid
    if state in cities:
        # Print the cities from the selected state
        print(f"Select a city from {state}:")
        for city in cities[state]:
            print(city)
    else:
        print("Invalid state entered. Please enter DC, VA, or MD.")

if __name__ == "__main__":
    main()


class weather():

    def getweather():
        """Scrapes the web for current weather info"""

        api_url = f'https://api.openweathermap.org/data/2.5/weather?lat=38.91982068626991&lon=-77.03656476393802&appid=8c6d96932235d74117595f9e8423547b'

        request = requests.get(api_url)

        json_convert = request.json()

        for x in json_convert:
            temperature = x['temp'] 
            fahrenheit = (temperature - 273.15) * 1.8 + 32
            humidity = x['humidity']
            print(f'{fahrenheit}: {humidity}')



        
    # Dc Coords: 38.91982068626991, -77.03656476393802
   
    def anaylzeweather(): 
        """Provides an analysis about the weather (DON)"""
        
        cur_weather = weather.getweather("Gaithersburg", "MD")
        
    
    def predictweather():
        """Makes predictions about future weather events"""
        pass
    
    def reccomend():
        """Reccomends to the user of how they can prepare for weather events (DON)"""
        pass
    
