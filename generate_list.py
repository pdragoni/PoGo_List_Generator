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
        print(f"Arquivo {input_file} não encontrado.")
        return

    list_type = input("Trade (1) or Delete (2)? ")
    if list_type == "1":
        format_str = "{id},"
    elif list_type == "2":
        format_str = "!{id}&"
    else:
        print("list_type not recognized. Use '1' or '2'.")
        return

    print("Selecione as regiões desejadas (separe por vírgula, ex: kanto,johto,hoenn):")
    print("Opções disponíveis:", ", ".join(regions))
    selected = input("Regiões: ").lower().replace(" ", "").split(",")
    selected = [r for r in selected if r in regions]
    if not selected or selected == [""]:
        selected = regions

    with open(output_file, "w", encoding="utf-8") as file:
        for id, data in pokemon_data.items():
            # Suporta múltiplas regiões por Pokémon
            poke_regions = data.get("regions", [])
            if any(region in poke_regions for region in selected):
                file.write(format_str.format(id=id))

    print(f"Dados salvos em {output_file}")

if __name__ == "__main__":
    process_pokemon_list()
