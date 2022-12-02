def projdi_vsechny_udaje(*args) -> None:
    for zaznam in args:
        if "end" in zaznam:  # if zaznam == "end":
            break
        else:
            jmeno, zbytek = rozdel_email(zaznam, ".")
            prijmeni, domena = rozdel_email(zbytek, "@")
            print(
                {"jmeno": jmeno, "prijmeni": prijmeni, "domena": domena}
            )


def rozdel_email(email: str, symbol: str) -> tuple:
    prvni_cast, zbytek = email.split(symbol, maxsplit=1)
    return (prvni_cast.title(), zbytek)



if __name__ == "__main__":
    print(
        projdi_vsechny_udaje(
            'petra.fulinova@firma.cz',
            'adela.vancurova@firma.cz',
            'andrea.hertlova@firma.cz',
            'petr.vyhnis@firma.cz',
            'jan.feckanin@firma.cz',
            'pavel.harant@firma.cz',
            'zdenka.bendova@firma.cz',
            'monika.miczova@firma.cz',
            'jan.mosquito@firma.cz',
            'barbora.suvova@firma.cz',
            'lenka.kafkova@firma.cz',
            'nikola.hoffmannova@firma.cz',
            'daniela.sedlakova@firma.cz',
            'ivana.jerabkova@firma.cz',
            'valeria.jagerska@firma.cz',
            'hana.bayerova@firma.cz',
            'tomas.zamecnik@firma.cz',
            'helena.strasilova@firma.cz',
            'jana.kralova@firma.cz',
            'hermina.duskova@firma.cz',
            'dana.mirgova@firma.cz',
            'end',
            '...'
        )
    )
