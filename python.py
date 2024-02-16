import requests

response = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=yK6WV9i70UXcRXLTKH68x0KViqYi2QAC3WOYa2gI')
print(response.status_code)
print(response.json)

img = response.json()['photos'][0]['img_src']
print(img)