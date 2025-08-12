import requests
import json

# Mapping of Pokémon numbers (as strings) to extra regions with forms
EXTRA_REGIONS = {
    # Kanto with Alola forms
    "19": ["alola"], "20": ["alola"], "26": ["alola"], "27": ["alola"], "28": ["alola"],
    "37": ["alola"], "38": ["alola"], "50": ["alola"], "51": ["alola"], "52": ["alola", "galar"],
    "53": ["alola"], "74": ["alola"], "75": ["alola"], "76": ["alola"], "88": ["alola"],
    "89": ["alola"], "103": ["alola"], "105": ["alola"],
    # Kanto with Galar forms
    "77": ["galar"], "78": ["galar"], "83": ["galar"], "110": ["galar"], "122": ["galar"],
    "144": ["galar"], "145": ["galar"], "146": ["galar"],
    # Kanto with Hisui forms
    "58": ["hisui"], "59": ["hisui"], "100": ["hisui"], "101": ["hisui"],
    # Johto with Galar/Hisui forms
    "211": ["hisui"], "215": ["hisui"], "222": ["galar"],
    # Hoenn with Galar forms
    "263": ["galar"], "264": ["galar"],
    # Unova with Galar/Hisui forms
    "549": ["hisui"], "550": ["hisui"], "554": ["galar"], "555": ["galar"], "562": ["galar"],
    "570": ["hisui"], "571": ["hisui"],
    # Kalos with Hisui forms
    "705": ["hisui"], "706": ["hisui"], "713": ["hisui"],
    # Alola with Hisui forms
    "724": ["hisui"],
}


def get_regions(number):
    """Retorna uma lista de regiões para o número do Pokémon."""
    number = int(number)
    regions = []
    if 1 <= number <= 151:
        regions.append("kanto")
    if 152 <= number <= 251:
        regions.append("johto")
    if 252 <= number <= 386:
        regions.append("hoenn")
    if 387 <= number <= 493:
        regions.append("sinnoh")
    if 494 <= number <= 649:
        regions.append("unova")
    if 650 <= number <= 721:
        regions.append("kalos")
    if 722 <= number <= 809:
        regions.append("alola")
    if 810 <= number <= 898:
        regions.append("galar")
    if 899 <= number <= 905:
        regions.append("hisui")
    if 906 <= number <= 1025:
        regions.append("paldea")
    # Add extra regions if present
    str_number = str(number)
    if str_number in EXTRA_REGIONS:
        for extra in EXTRA_REGIONS[str_number]:
            if extra not in regions:
                regions.append(extra)
    if not regions:
        regions.append("unknown")
    return regions


def fetch_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit=1025"
    file = "pokemon_list.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        pokemon_data = response.json()

        pokemon_dict = {}

        for pokemon in pokemon_data["results"]:
            name = pokemon["name"]
            url = pokemon["url"]
            number = url.rstrip('/').split('/')[-1]
            regions = get_regions(number)
            pokemon_dict[number] = {"name": name, "regions": regions}

        with open(file, "w", encoding="utf-8") as f:
            json.dump(pokemon_dict, f, indent=4, ensure_ascii=False)

        print("Pokemon data fetched and saved successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


if __name__ == "__main__":
    fetch_pokemon()
