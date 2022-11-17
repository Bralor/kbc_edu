pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]  # ['g']

print("Začátek:", ", ".join(pismena))

while len(pismena) > 0:  # while pismena:
    vstup_uzivatele = input("Zadej písmeno: ".upper())  # 'g'

    if vstup_uzivatele in pismena:
        pismena.remove(vstup_uzivatele)
    else:
        print(vstup_uzivatele, ", není součástí písmen!", sep="")

    if len(pismena) != 0:  # II. varianta, bez 'break'
        print("Zbývající písmena:", ", ".join(pismena))

else:
    print("Seznam je prázdný, vyhráváš!")

# if len(pismena) == 0:  # I. varianta, s 'break'
#     break
# else:
#     print("Zbývající písmena:", ", ".join(pismena))
