import requests
url = 'https://rickandmortyapi.com/api/character'

payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

respuesta_json =response.json()
#print (respuesta_json['info'])
personajes= (respuesta_json['results'])
for person in personajes:
    print (f"The character {person['name']} is {person['status']}")
