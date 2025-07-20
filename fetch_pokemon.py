import requests
import json


def fetch_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit=1025"
    file = "pokemon_list.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)
        pokemon_data = response.json()
        # print(pokemon_data)
        
        pokemon_dict = {}
        
        for pokemon in pokemon_data["results"]:
            name = pokemon["name"]
            url = pokemon["url"]
            
            number = url.rstrip('/').split('/')[-1]
            
            # print(f"{number}: {name}")
            
            pokemon_dict[number] = name

        # Save data to a JSON file
        with open("pokemon_list.json", "w", encoding="utf-8") as file:
            json.dump(pokemon_dict, file, indent=4, ensure_ascii=False)

        # print("Data saved to pokemon_list.json")
        print("Pokemon data fetched and saved successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


if __name__ == "__main__":
    fetch_pokemon()
