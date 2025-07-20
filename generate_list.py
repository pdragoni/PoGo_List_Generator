import json

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
    # Definição do formato de escrita conforme a lista desejada
    if list_type == "1":
        format_str = "{id},"
    elif list_type == "2":
        format_str = "!{id}&"
    else:
        print("list_type not recognized. Use '1' or '2'.")
        return

    # Escrita no arquivo (usando apenas as chaves do dict)
    with open(output_file, "w", encoding="utf-8") as file:
        for id in pokemon_data.keys():
            file.write(format_str.format(id=id))

    print(f"Dados salvos em {output_file}")

# Entrada do usuário
if __name__ == "__main__":
    process_pokemon_list()
