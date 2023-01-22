import requests
token = 'eab2f7d0143e9160c73e2b5db57b2ee3'

response = requests.post('https://pokemonbattle.me:5000/pokemons', 
headers = {'Content-Type': 'application/json', 'trainer_token': token},
json = {
    "name": "Генг",
    "photo": "https://flyclipart.com/thumb2/imagen-806302.png"
    })

print(response.text)

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', 
headers = {'Content-Type': 'application/json', 'trainer_token': token},
json = {
    "pokemon_id": "3238",
    "name": "Генгар",
    "photo": "https://i.pinimg.com/originals/40/18/38/40183856ce85f564515223bb3ba8f5f3.png"
    })

print(response_change.text)

response_add_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', 
headers = {'Content-Type': 'application/json', 'trainer_token': token},
json = {"pokemon_id": "3238",})

print(response_add_pokeball.text)
