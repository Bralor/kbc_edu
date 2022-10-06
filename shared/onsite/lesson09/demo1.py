import os
import ssl
import smtplib
from email.message import EmailMessage


def nachystej_hlavicku(odesilatel: str, adresat: str, predmet: str):
    email = EmailMessage()
    email['From'] = odesilatel
    email['To'] = adresat
    email['Subject'] = predmet
    return email


def main():
    odesilatel = "engeto.lekce09@gmail.com"
    adresat = "me@matousholinka.com"

    email = nachystej_hlavicku(
        odesilatel=odesilatel,
        adresat=adresat,
        predmet="Lekce09, demo1, automatizace pro odesílání emailů"
    )
    email.set_content("""Posílám ti svoji první zprávu. Pomocí Pythonu!!^.^ Yes""")


    with smtplib.SMTP_SSL(
            'smtp.gmail.com',
            context=ssl.create_default_context()
    ) as smtp:
        smtp.login(odesilatel, os.getenv("demo_password"))
        smtp.sendmail(odesilatel, adresat, email.as_string())


if __name__ == "__main__":
    main()
