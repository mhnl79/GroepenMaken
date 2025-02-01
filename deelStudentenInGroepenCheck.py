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

    while True:
        # Groepen maken
        groepen = []
        random.shuffle(studenten)  # Willekeurig schudden van de studentenlijst
        
        # Initialiseer lege groepen
        aantal_groepen = (len(studenten) + groepsgrootte - 1) // groepsgrootte  # Ronde omhoog
        for _ in range(aantal_groepen):
            groepen.append([])

        # Verdeel studenten over de groepen
        student_index = 0
        for student in studenten:
            groepen[student_index % aantal_groepen].append(student)
            student_index += 1

        # Controleer of er groepen zijn met alleen dezelfde functie
        ongeldig = False
        for groep in groepen:
            if len(groep) > 1:
                functies = set()  # Maak een lege set om de functies in de groep op te slaan
                for student in groep:
                    functies.add(student['functie'])  # Voeg de functie van de student toe aan de set
                if len(functies) == 1:  # Controleer of de set slechts één unieke functie bevat
                    ongeldig = True  # Als dat zo is, markeer de verdeling als ongeldig
                    break  # Stop de lus omdat we een ongeldige situatie hebben gevonden
        
        # Als er geen ongeldige groepen zijn, breek de lus
        if not ongeldig:
            break

    # Groepen weergeven
    for i, groep in enumerate(groepen):
        print(f"Groep {i + 1}:")
        for student in groep:
            print(f"  {student['voornaam']} {student['tussenvoegsels']} {student['achternaam']} ({student['functie']})")
        print()

# Script uitvoeren
laad_studenten_en_maak_groepen()

