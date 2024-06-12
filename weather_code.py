import requests

api_key = open('.....', 'r').read()

while True:
    location = input("Location: ")

    result = requests.get(f'.....')
    if result.json()['cod'] == '404':
        print("Invalid location!")
        continue
    break

description = result.json()['weather'][0]['description']
temperature = round(result.json()['main']['temp'])
feels_like = round(result.json()['main']['feels_like'])
high = round(result.json()['main']['temp_max'])
low = round(result.json()['main']['temp_min'])

print(f"The weather in {location[0].upper()}{location[1:]} is {temperature}° C with {description}.")
print(f"It feels like {feels_like}° C.")
print(f"Today's high is {high}° C and today's low is {low}° C.")