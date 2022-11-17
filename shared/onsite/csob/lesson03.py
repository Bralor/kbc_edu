sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
oddelovac = "=" * 62
film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}

film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}

film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}

# sjednoť předchozí 3 slovníky do jednoho slovníku 'filmy'
filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3
}

print(
    "Vitejte v nasem filmovem slovniku!".upper().center(62),
    oddelovac,sep="\n"
)
print(f"| {' | '.join(sluzby)} |".center(62), oddelovac, sep="\n")

vyber = input("Vyber sluzbu:")

if vyber in sluzby and vyber == "dostupne filmy":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())),
          oddelovac, sep="\n")

elif vyber in sluzby and vyber == "detaily filmu":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), sep="\n")
    film = input("Vyber film:")
    print(oddelovac, f"FILM: {film}", filmy.get(film), oddelovac, sep="\n")

else:
    print("vybrana sluzba neni v nabidce, ukoncuji..")

