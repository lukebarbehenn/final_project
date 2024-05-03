# INST326 Final Project 

from bs4 import BeautifulSoup
import requests

class weather():

    def getweather(city, state):
        """Scrapes the web for current weather info"""

        api_url = f'https://weather.com/weather/tenday/l/{city}+{state}'

        request = requests.get(api_url)

        soup = BeautifulSoup(request.text, 'html.parser')

        weather = soup.find('div')

        print(weather)
    
   

    
    def anaylzeweather(): 
        """Provides an analysis about the weather (DON)"""
        
        cur_weather = weather.getweather("Gaithersburg", "MD")
        
    
    def predictweather():
        """Makes predictions about future weather events"""
        pass
    
    def reccomend():
        """Reccomends to the user of how they can prepare for weather events (DON)"""
        pass
    
