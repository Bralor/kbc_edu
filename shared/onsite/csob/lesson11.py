# 

import sys
import csv
import json


def nacti_json(jmeno_souboru: str):
    with open(jmeno_souboru, mode="r", encoding="utf-8") as json_soubor:
        return json.load(json_soubor)


def zapis_csv(jmeno_csv: str, data_zamestnancu: list):
    with open(jmeno_csv, mode="w", encoding="utf-8") as csv_soubor:
        zapisovac = csv.DictWriter(csv_soubor,
                                   fieldnames=data_zamestnancu[0].keys())

        zapisovac.writeheader()
        zapisovac.writerows(data_zamestnancu)  # NEBO: writerow()


if __name__ == "__main__":
    jmeno_json = sys.argv[1]
    jmeno_csv = sys.argv[2]

    zadana_data = nacti_json(jmeno_json)  # sys.argv[1] -> jmeno JSON
    zapis_csv(jmeno_csv, zadana_data)     # sys.argv[2] -> jmeno CSV
