import os
import ssl
import smtplib
from pathlib import Path
from string import Template
from email.message import EmailMessage


def nachystej_hlavicku(odesilatel: str, adresat: str, predmet: str):
    email = EmailMessage()
    email['From'] = odesilatel
    email['To'] = adresat
    email['Subject'] = predmet
    return email


def precti_sablonu(cesta: str):
    return Path(cesta).read_text()


def nahrad_hodnoty(obsah: str, **kwargs):
    text = Template(obsah)
    return text.substitute(kwargs)


def pridej_prilohu(email, jmeno_souboru: str):
    with open(jmeno_souboru, mode="rb") as ntb:
        file_data = ntb.read()

    email.add_attachment(
        file_data,
        maintype='application',
        subtype='ipynb',
        filename='lesson09.ipynb'
    )
    return email


def main():
    odesilatel = "engeto.lekce09@gmail.com"
    adresat = "me@matousholinka.com"

    email = nachystej_hlavicku(
        odesilatel=odesilatel,
        adresat=adresat,
        predmet="Lekce09, demo3, automatizace pro odesílání emailů."
    )

    email.set_content(
        nahrad_hodnoty(
            precti_sablonu("index.html"),
            jmeno="Matouš",
            lekce="lekce09"
        ),
        "html"
    )

    email = pridej_prilohu(email, "lesson09.ipynb")

    with smtplib.SMTP_SSL(
            'smtp.gmail.com',
            context=ssl.create_default_context()
    ) as smtp:
        smtp.login(odesilatel, os.getenv("demo_password"))
        smtp.sendmail(odesilatel, adresat, email.as_string())


if __name__ == "__main__":
    main()
