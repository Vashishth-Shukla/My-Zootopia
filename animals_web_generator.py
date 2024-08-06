import json


def load_data(file_path):
    """
    Loads a JSON file

    Args:
        file_path (str): The path to the JSON file to be loaded.

    Returns:
        dict: The data loaded from the JSON file.

    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_output_data(data):
    """
    From the animal data returns the specific output data

    Args:
        data (list of dict): The row animal data.

    Returns:
        output_data (list of dict): Selected data
    """
    output_data = []
    for animal in data:
        animal_data = {}
        animal_data["Name"] = animal["name"]
        animal_data["Diet"] = animal["characteristics"]["diet"]
        animal_data["Location"] = animal["locations"]
        if "type" in animal["characteristics"]:
            animal_data["Type"] = animal["characteristics"]["type"]
        output_data.append(animal_data)
    return output_data


def print_output_data(data):
    """
    Prints the data in a format

    Args:
        data (list of dict): the selected animal data to be printed
    """
    for animal in data:
        for key, value in animal.items():
            if isinstance(value, list):
                print(f"{key}: {', '.join(value)}")
            else:
                print(f"{key}: {value}")
        print()


# def get_string_data(data):
#     """
#     Returns the string of animal data

#     Args:
#         data(list of dict): the selected animal data to be printed

#     Returns:
#         string_data(string): the selected animal data in a string
#     """
#     string_data = r"<pre>"
#     for animal in data:
#         string_data += '<li class="cards__item">'
#         for key, value in animal.items():
#             if isinstance(value, list):
#                 string_data += f"{key}: {', '.join(value)}<br/>\n"
#             else:
#                 string_data += f"{key}: {value}<br/>\n"
#     string_data += r"</pre>"
#     return string_data


def get_string_data(data):
    """
    Returns the string of animal data in the specified HTML format.

    Args:
        data(list of dict): the selected animal data to be printed

    Returns:
        string_data (string): the selected animal data in a formatted HTML string
    """
    string_data = ""
    for animal in data:
        string_data += '<li class="cards__item">\n'
        string_data += f'  <div class="card__title">{animal["Name"]}</div>\n'
        string_data += '  <p class="card__text">\n'
        string_data += (
            f'      <strong>Location:</strong> {", ".join(animal["Location"])}<br/>\n'
        )
        if "Type" in animal:
            string_data += f'      <strong>Type:</strong> {animal["Type"]}<br/>\n'
        string_data += f'      <strong>Diet:</strong> {animal["Diet"]}<br/>\n'
        string_data += "  </p>\n"
        string_data += "</li>\n"
    return string_data


def replace_animal_info(animal_data_string):
    """
    Replaces the placeholder text with the animal data string.

    Args:
        animal_data_string(str): The string to place in HTML
    """
    with open("animals_template.html", "r") as html_file:
        html_data = html_file.read()
    html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", animal_data_string)
    with open("animals.html", "w") as out_file:
        out_file.write(html_data)
    print("HTML file created!")


def main():
    animals_data = load_data("animals_data.json")
    output_data = get_output_data(animals_data)
    # print_output_data(output_data)
    animal_string_data = get_string_data(output_data)
    replace_animal_info(animal_string_data)


if __name__ == "__main__":
    main()
