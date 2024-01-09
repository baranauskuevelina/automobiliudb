import json


def save_to_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []


# Load existing data from file
automobiliai = load_from_file("masinos.db")

while True:
    pasirinkimas = int(input("1 - įvesti automobilį\n2 - paieška\n3 - atvaizduoti automobilius\n0 - išeiti\n"))

    if pasirinkimas == 1:
        print("Įveskite automobilį:")
        marke = input("Markė: ")
        modelis = input("Modelis: ")
        spalva = input("Spalva: ")
        metai = int(input("Metai: "))
        kaina = float(input("Kaina: "))
        automobilis = {'id': len(automobiliai) + 1, 'marke': marke, 'modelis': modelis, 'spalva': spalva,
                       'metai': metai, 'kaina': kaina}
        automobiliai.append(automobilis)
        save_to_file("masinos.db", automobiliai)

    elif pasirinkimas == 2:
        # Code for option 2 goes here
        pass

    elif pasirinkimas == 3:
        print(automobiliai)

    elif pasirinkimas == 0:
        print("Viso gero")
        break
