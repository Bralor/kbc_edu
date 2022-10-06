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


def main():
    odesilatel = "engeto.lekce09@gmail.com"
    adresat = "me@matousholinka.com"

    email = nachystej_hlavicku(
        odesilatel=odesilatel,
        adresat=adresat,
        predmet="Lekce09, demo2, automatizace pro odesílání emailů"
    )
    email.set_content(
        nahrad_hodnoty(
            precti_sablonu("shared/onsite/lesson09/index.html"),
            jmeno="Matouš",
            lekce="lekce09"
        ),
        "html"
    )

    with smtplib.SMTP_SSL(
            'smtp.gmail.com',
            context=ssl.create_default_context()
    ) as smtp:
        smtp.login(odesilatel, os.getenv("demo_password"))
        smtp.sendmail(odesilatel, adresat, email.as_string())


if __name__ == "__main__":
    main()
