from requests import Response, get as requests_get
import json

ID: int = 10
URL: str = f'https://pokeapi.co/api/v2/pokemon/{ID}'
HEADERS: dict = {"Content-Type": "application/json"}

response: Response = requests_get(URL)

if response.status_code == 200:
    pokemon_data = response.json()

    with open(f'pokemon_{ID}.json', 'w') as f:
        json.dump(pokemon_data, f, indent=4)
else:
    print(f"Failed to retrieve data for Pokemon with ID {ID}")
