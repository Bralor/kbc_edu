# vstupni promenne
mesta = [
    "Praha", "Viden", "Olomouc",
    "Svitavy", "Zlin", "Ostrava"
]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180"""

# pozdravit uzivatele
# vypsat nabidku
print(
    "VITEJTE U NASI APLIKACE DESTINATIO!",
    cara,
    nabidka,
    cara,
    sep="\n"
)

# ziskat vstupy od uzivatele
destinace = input("CISLO DESTINACE:")
jmeno = input("JMENO:")
prijmeni = input("PRIJMENI:")
email = input("EMAIL:")
print(cara)

# propojit vstup a zadane hodnoty
upravena_destinace = mesta[int(destinace) - 1]
cena = ceny[int(destinace) - 1]

# vypis informace uzivateli
print(f"""DEKUJI, {jmeno} ZA OBJEDNAVKU,
CIL. DESTINACE: {upravena_destinace}, CENA JIZDNEHO: {cena},
NA TVUJ MAIL {email} JSME TI POSLALI LISTEK.""")
