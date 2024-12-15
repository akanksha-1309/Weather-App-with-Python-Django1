import requests

api_key = '45b01a7f6a9893cc9370a6fd91f105fb'  # Replace with your API key
city = 'London'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("API key is working!")
    print(f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C")
else:
    print("Error:", data['message'])
