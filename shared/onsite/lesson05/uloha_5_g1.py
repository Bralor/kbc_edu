pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]
pocet_pokusu = 20

print("Začátek: ", ", ".join(pismena), sep="")

while len(pismena) != 0:  # while pismena:
    zadani_uzivatele = input("Zadej písmeno v listu:")

    if zadani_uzivatele in pismena:
        pismena.remove(zadani_uzivatele)
        print(", ".join(pismena))
    else:
        print(zadani_uzivatele, "není součástí písmen!")

else:
    print("Seznam je prázdný! Vyhráváš!")  # "Konec hry!"

if pismena and pocet_pokusu == 0:

elif not pismena and pocet_pokusu != 0:

