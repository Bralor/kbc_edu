import csv
import json


def cti_json(jmeno_souboru: str) -> list:
    with open(jmeno_souboru, mode="r", encoding="utf-8") as json_zam:
        return json.load(json_zam)


def zapis_csv(jmeno_csv: str, obsah_csv: list):
    with open(jmeno_csv, mode="w", encoding="utf-8") as csv_v:
        zapisovac = csv.DictWriter(csv_v, fieldnames=obsah_csv[0].keys())
        zapisovac.writeheader()
        zapisovac.writerows(obsah_csv)


if __name__ == "__main__":
    nacteny_json = cti_json("zamestnanci.json")
    zapis_csv("vystup.csv", nacteny_json)
