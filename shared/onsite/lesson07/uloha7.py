import csv
import json


def main() -> None:
    """
    Hlavni funkce, ktera:
    1. Nacte data z JSON souboru,
    2. zapise nacteny obsah do CSV souboru.
    """
    json_cont = (read_json("zamestnanci.json"))
    write_csv("vysledek.csv", json_cont)


def read_json(filename: str) -> list:
    """
    Nacti data ze JSON souboru.
    """
    with open(filename, encoding="utf-8") as json_:
        return json.load(json_)


def write_csv(filename: str, content: list) -> None:
    """
    Zapis obsah libovolneho souboru do souboru typu CSV.
    """
    with open(filename, mode="w", encoding="utf-8") as csv_:
        writter = csv.DictWriter(csv_, fieldnames=content[0].keys())
        writter.writeheader()
        writter.writerows(content)



if __name__ == "__main__":
    main()
