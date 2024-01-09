automobiliai = []

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

    elif pasirinkimas == 2:
        marke = input("Markė: ").lower()
        modelis = input("Modelis: ").lower()
        spalva = input("Spalva: ").lower()
        metai_nuo = input("Metai nuo: ")
        metai_nuo = int(metai_nuo) if metai_nuo else 1900
        metai_iki = input("Metai iki: ")
        metai_iki = int(metai_iki) if metai_iki else 2100
        kaina_nuo = input("Kaina nuo: ")
        kaina_nuo = float(kaina_nuo) if kaina_nuo else 0
        kaina_iki = input("Kaina iki: ")
        kaina_iki = float(kaina_iki) if kaina_iki else 10000000

        rezultatai = [auto for auto in automobiliai if
                      marke in auto['marke'].lower() and
                      modelis in auto['modelis'].lower() and
                      spalva in auto['spalva'].lower() and
                      metai_nuo <= auto['metai'] <= metai_iki and
                      kaina_nuo <= auto['kaina'] <= kaina_iki]

        print(rezultatai)

    elif pasirinkimas == 3:
        print(automobiliai)

    elif pasirinkimas == 0:
        print("Viso gero")
        break
