import json

regions = [
    "kanto", "johto", "hoenn", "sinnoh", "unova",
    "kalos", "alola", "galar", "hisui", "paldea"
]

def process_pokemon_list():
    input_file = "pokemon_list.json"
    output_file = "final_list.txt"
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            pokemon_data = json.load(file)
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        return

    list_type = input("Trade (1) or Delete (2)? ")
    if list_type == "1":
        format_str = "{id},"
    elif list_type == "2":
        format_str = "!{id}&"
    else:
        print("list_type not recognized. Use '1' or '2'.")
        return

    print("Select the desired regions (separate by commas, e.g., kanto,johto,hoenn):")
    print("Available options:", ", ".join(regions))
    selected = input("Regions: ").lower().replace(" ", "").split(",")
    selected = [r for r in selected if r in regions]
    if not selected or selected == [""]:
        selected = regions

    only_special = input("Legendary, Mythical, and/or similar Pokémon? (y/n): ").lower() == "y"
    only_common = False
    if only_special:
        only_common = input("Show common Pokémon too? (y/n): ").lower() == "y"
    else:
        only_common = True

    only_shiny = input("Only shiny Pokémon? (y/n): ").lower() == "y"

    with open(output_file, "w", encoding="utf-8") as file:
        for id, data in pokemon_data.items():
            poke_regions = data.get("regions", [])
            if not any(region in poke_regions for region in selected):
                continue

            is_special = "special_category" in data
            is_shiny = data.get("shiny", False)

            # 1. only_special True & only_shiny True: apenas special_category e shiny: True
            if only_special and not only_common and only_shiny:
                if is_special and is_shiny:
                    file.write(format_str.format(id=id))
                continue

            # 2. only_special True & only_common True & only_shiny True: todos shiny
            if only_special and only_common and only_shiny:
                if is_shiny:
                    file.write(format_str.format(id=id))
                continue

            # 3. only_special True & only_common True & only_shiny False: todos não shiny
            if only_special and only_common and not only_shiny:
                if not is_shiny:
                    file.write(format_str.format(id=id))
                continue

            # 4. only_special False & only_shiny True: comuns shiny
            if not only_special and only_shiny:
                if not is_special and is_shiny:
                    file.write(format_str.format(id=id))
                continue

            # 5. only_special False & only_shiny False: comuns não shiny
            if not only_special and not only_shiny:
                if not is_special and not is_shiny:
                    file.write(format_str.format(id=id))
                continue

            # 6. only_special True & only_common False & only_shiny True: special_category shiny
            if only_special and not only_common and only_shiny:
                if is_special and is_shiny:
                    file.write(format_str.format(id=id))
                continue

            # 7. only_special True & only_common False & only_shiny False: special_category não shiny
            if only_special and not only_common and not only_shiny:
                if is_special and not is_shiny:
                    file.write(format_str.format(id=id))
                continue

    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    process_pokemon_list()
