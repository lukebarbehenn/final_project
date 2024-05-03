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
    
