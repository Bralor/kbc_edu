import datetime

from psutil import sensors_battery


def napis_zpravu(cas, obsah):
    return f"{cas}: INFO: {obsah}\n"


def ziskej_stav_baterie():
    return str(
        round(
            sensors_battery().percent,
            2
        )
    )


def zapis_zpravu_do_souboru(jmeno: str, zprava: str):
    with open(jmeno, mode="a", encoding="utf-8") as txt:
        txt.write(zprava)
        

def main():
    state_1 = ziskej_stav_baterie()
    msg_1 = napis_zpravu(
        cas=datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"),
        obsah=f"Stav baterie: {state_1}"
    )
    zapis_zpravu_do_souboru(
        jmeno="stav_baterie.txt",
        zprava=msg_1
    )


if __name__ == "__main__":
    main()
