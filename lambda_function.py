import json
import requests


def lambda_handler(event, context):


    # Parsing body dari event (string ke dict)
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        return {"message": "Bad Request, no body found"}


    # Mendapatkan nilai 'city' dari body
    city = body.get('city')
    if not city:
        return {"message": "City is required"}


    # Panggil weather service di EC2
    url = "http://10.0.0.251:8080/function/weather"
    try:
        response = requests.post(url, json={"city": city})
        weather_data = response.json()


        # Konversi dari Celcius ke Fahrenheit
        celsius = float(weather_data['temperature'][:-2])
        fahrenheit = (celsius * 9/5) + 32
        weather_data['temperature'] = f"{fahrenheit:.1f}ºF"


        # Langsung return JSON dalam bentuk dictionary
        return {
            "city": weather_data['city'],
            "temperature": weather_data['temperature'],
            "condition": weather_data['condition']
        }


    except requests.exceptions.RequestException as e:
        return {"message": "Error contacting weather service", "error": str(e)}
