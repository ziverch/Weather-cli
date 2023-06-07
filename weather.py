import datetime as dt
import requests

# def temperature(city):
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = '82026fb156053a8b33fcc50b35f403b1'
while True:
    try:
        city_name = input("What is the city's name: ")
        parameters = {
            "q": city_name,
            "appid": API_KEY,
            "units": "metric",
        }
        response = requests.get(BASE_URL, params=parameters)
        response.raise_for_status()
        data = response.json()
        country_name = data['sys']['country']

        break
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print("City not found. Enter a valid city")
        else:
            print("Error occurred while retrieving weather data\n", e)



def temperature (city):
    temp_in_celsius = (data['main']['temp'])
    temp_in_fahrenheit = temp_in_celsius * (9/5) + 32
    temp_it_feels_like = data['main']['feels_like']
    weather_description = data['weather'][0]['description']
    degree_sign = chr(176)
    print(f"it's {temp_in_celsius: .1f}{degree_sign}C in {city_name}, {country_name}\n"
          f"That's {temp_in_fahrenheit:.1f}{degree_sign}F in freedom units")
    print(f"it feels more like{temp_it_feels_like: .1f}{degree_sign}C")
    print(f"weather description: {weather_description}")


def check_city_humidity (city):
    humidity = data['main']['humidity']
    if humidity >= 70:
        print(f"Expect a lot of moisture, around {humidity}%")
    elif 50 <= humidity <= 69:
        print(f"it's moderately humid today, with humidity at {humidity}%")
    else:
        print(f"it's around {humidity}% today")


def sunset_sunrise (city):
    sunset = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    sunrise = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    print(f"Sun rise in {city} at {sunrise}, local time.")
    print(f"The Sun will set at {sunset}, local time.")

print()
print("1. get temperature info\n"
      "2. get humidity and pressure\n"
      "3. get sunrise, sunset time")

while True:
    try:
        usr_choice = int(input("select from the options above: "))
        print()
        if usr_choice == 1:
            temperature(city_name)
        elif usr_choice == 2:
            check_city_humidity(city_name)
        elif usr_choice == 3:
            sunset_sunrise(city_name)
        else:
            print("Invalid option")
        break
    except ValueError:
        print("Enter a correct option")