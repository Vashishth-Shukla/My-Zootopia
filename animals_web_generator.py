import json


def load_data(file_path):
    """Loads a JSON file

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
    """Prints the data in a format

    Args:
        data (list of dict): the selected animal data to be printed
    """
    for animal in data:
        for key, value in animal.items():
            if key == "Location":
                print(f"{key}: {', '.join(value)}")
            else:
                print(f"{key}: {value}")
        print()


def main():
    animals_data = load_data("animals_data.json")
    output_data = get_output_data(animals_data)
    print_output_data(output_data)


if __name__ == "__main__":
    main()
