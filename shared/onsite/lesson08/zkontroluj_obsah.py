import pathlib


def zobraz_obsah_adresare(cesta: str) -> list:
    aktualni_adr = pathlib.Path(cesta)
    return [
        soubor.name
        for soubor in aktualni_adr.iterdir()
    ]


def zapis_soubory(jmeno_soubor: str, obsah_souboru: list) -> None:
    with open(jmeno_soubor, mode="a", encoding="utf-8") as txt:
        txt.writelines(f"{', '.join(obsah_souboru)}\n")


def spoustec():
    """
    Funkce zabali spousteni dvou predchozich funkci a vytvori textovy soubor
    se soubory v preddefinovanem adresari.
    """
    obsah = zobraz_obsah_adresare(
        "/home/matous/projects/kbc_edu/shared/onsite/lesson08"
    )
    zapis_soubory(
        "/home/matous/projects/kbc_edu"
        "/shared/onsite/lesson08/seznam_souboru.txt",
        obsah
    )


if __name__ == "__main__":
    spoustec()
