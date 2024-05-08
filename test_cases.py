# Test cases for non-input functions of our fp_code script 

from fp_code import Weather

def test_get_weather():

    """Tests the getweather function, passing in different latitudes and longitudes of locations"""

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

    assert Weather.get_weather(dc_lat, dc_lon)
    assert Weather.get_weather(arl_lat, arl_lon)
    assert Weather.get_weather(alx_lat, alx_lon)
    assert Weather.get_weather(bsd_lat, bsd_lon)
    assert Weather.get_weather(cp_lat, cp_lon)

def test_analyze_weather():

    """Tests the analyze weather function, passing in different temperatures and humidities"""

    assert Weather.analyze_weather(100, 90) == "Weather is very hot and highly humid."
    assert Weather.analyze_weather(80, 90) == "Weather is moderately hot and highly humid."
    assert Weather.analyze_weather(60, 90) == "Weather is mild and highly humid."
    assert Weather.analyze_weather(40, 90) == "Weather is cold and highly humid."
    assert Weather.analyze_weather(30, 90) == "Weather is very cold and highly humid."

    assert Weather.analyze_weather(100, 70) == "Weather is very hot and moderately humid."
    assert Weather.analyze_weather(80, 70) == "Weather is moderately hot and moderately humid."
    assert Weather.analyze_weather(60, 70) == "Weather is mild and moderately humid."
    assert Weather.analyze_weather(40, 70) == "Weather is cold and moderately humid."
    assert Weather.analyze_weather(30, 70) == "Weather is very cold and moderately humid."

    assert Weather.analyze_weather(100, 40) == "Weather is very hot and dry."
    assert Weather.analyze_weather(80, 40) == "Weather is moderately hot and dry."
    assert Weather.analyze_weather(60, 40) == "Weather is mild and dry."
    assert Weather.analyze_weather(40, 40) == "Weather is cold and dry."
    assert Weather.analyze_weather(30, 40) == "Weather is very cold and dry."

def test_recomend():

    """Tests the recomend function, passing in different temperatures and weather events"""

    assert Weather.recommend(60, "rain") == "It's going to rain; don't forget to carry an umbrella!"
    assert Weather.recommend(60, "drizzle") == "It's going to rain; don't forget to carry an umbrella!"
    assert Weather.recommend(60, "mist") == "It's going to rain; don't forget to carry an umbrella!"
    
    assert Weather.recommend(30, "sun") == "It's very cold; make sure to wear heavy winter clothes."
    assert Weather.recommend(100, "sun") == "It's very hot; stay hydrated and avoid going out during peak hours."
    assert Weather.recommend(70, "sun") == "Weather looks nice; you should be good!"
    
# Function Calls 
test_get_weather()
test_analyze_weather()
test_recomend()

