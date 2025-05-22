import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'YOUR-TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}


BODY_CREATE = {"name": "standart", "photo_id": 444}
response_create = requests.post(url=f'{URL}pokemons', headers=HEADER, json=BODY_CREATE)
print("Ответ на создание:", response_create.text)


pokemon_data = response_create.json()  
pokemon_id = pokemon_data.get('id')    


BODY_PUT = {"pokemon_id": pokemon_id, "name": "generate", 'photo_id': -1}
response_put = requests.put(url=f'{URL}pokemons', headers=HEADER, json=BODY_PUT)
print("Ответ на обновление:", response_put.text)


BODY_pokeball = {"pokemon_id": pokemon_id}
response_pokeball = requests.post(url=f'{URL}trainers/add_pokeball', headers=HEADER, json=BODY_pokeball)
print("Ответ на поимку:", response_put.text)
