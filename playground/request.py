import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"

pokemon_name = "charmander"

url = f"{base_url}{pokemon_name}"

response = requests.get(url)

if response.status_code == 200:
    pokemon_data = response.json()
    attack = pokemon_data['stats'][4]['base_stat']
    defense = pokemon_data['stats'][3]['base_stat']
    print(f"Attack: {attack}, Defense: {defense}")
else:
    print("Failed to retrieve data from the API")
