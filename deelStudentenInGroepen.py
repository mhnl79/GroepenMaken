import csv
import random

# Functie om studenten uit een CSV-bestand te laden en groepen te maken
def laad_studenten_en_maak_groepen():
    # Studenten laden
    studenten = []
    with open('studenten.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            studenten.append(row)

    while True:
        try:
            groepsgrootte = int(input(f"Geef de groepsgrootte op (max {len(studenten)}): "))
            if 1 <= groepsgrootte <= len(studenten):
                break
            else:
                print(f"Ongeldige groepsgrootte. Kies een getal tussen 1 en {len(studenten)}.")
        except ValueError:
            print("Ongeldige invoer. Probeer het opnieuw.")

    # Groepen maken
    groepen = []
    random.shuffle(studenten)  # Willekeurig schudden van de studentenlijst
    
    # Initialiseer lege groepen
    for _ in range(0, len(studenten), groepsgrootte):
        groepen.append([])

    # Verdeel studenten over de groepen
    for student in studenten:
        for groep in groepen:
            if len(groep) < groepsgrootte:
                groep.append(student)
                break
    
    # Groepen weergeven
    for i, groep in enumerate(groepen):
        print(f"Groep {i + 1}:")
        for student in groep:
            print(f"  {student['voornaam']} {student['tussenvoegsels']} {student['achternaam']} ({student['functie']})")
        print()

# Script uitvoeren
laad_studenten_en_maak_groepen()
