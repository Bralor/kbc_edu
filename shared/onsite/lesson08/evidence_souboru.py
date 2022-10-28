import os
import datetime


def vypis_zaznam(cas: str, vystup: list) -> str:
    """
    Funkce vypíše zprávu o stavu souborů v konkrétním čase.
    """
    return f"{cas}: {', '.join(vystup)}\n"


def zapis_do_txt(jmeno: str, obsah: str) -> None:
    """
    Funkce vytvoří nebo rozšíří textový soubor o nový záznam.
    """
    with open(jmeno, mode="a", encoding="utf-8") as txt:
        txt.write(obsah)


if __name__ == "__main__":
    zaznam = vypis_zaznam(
        cas=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        vystup=os.listdir(
                    "/home/matous/projects/kbc_edu/shared/onsite/lesson08"  # potřeba změnit
        )
    )
    zapis_do_txt(
        "/home/matous/projects/kbc_edu/shared/onsite/lesson08/stav_adr.txt",  # potřeba změnit
        zaznam
    )