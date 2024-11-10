import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd888b0179a1418502a67a1bcd77b2abe'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "savchencko.kseniia@yandex.ru",
    "password": "SamKami0202"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "128154",
    "name": "Vhagar",
    "photo_id": 1
}

body_pokeball = {
    "pokemon_id": "128154"
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json = body_create)
print(response_create.text)'''

'''response_name = requests.put(url = f'{URL}/pokemons', headers=HEADER, json = body_name)
print(response_name.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json = body_pokeball)
print(response_pokeball.text)