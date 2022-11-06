import os
import ssl
import smtplib
from string import Template
from email.message import EmailMessage


def nachystej_email(odesilatel: str, adresati: list, predmet: str):
    """
    Funkce vracející nachystaný objekt, který reprezentuje skutečnou
    emailovou zprávu.
    """
    email = EmailMessage()
    email['From'] = odesilatel
    email['To'] = adresati
    email['Subject'] = predmet
    return email


def precti_html_predlohu(jmeno_souboru: str):
    with open(jmeno_souboru, mode="r", encoding="utf-8") as html:
        return html.read()


def nahrad_promenne_v_textu(text: str, **kwargs):
    sablona = Template(text)
    return sablona.substitute(kwargs)


def pridej_prilohu(email, jmeno_souboru: str):
    with open(jmeno_souboru, mode="rb") as ipynb:
        obsah = ipynb.read()

    email.add_attachment(
        obsah,
        maintype="text/plain",  # "application",
        subtype="ipynb",
        filename=jmeno_souboru
    )

    return email


def main():
    context = ssl.create_default_context()
    odesilatel = "engeto.lekce09@gmail.com"
    adresati = "me@matousholinka.com"

    email = nachystej_email(
        odesilatel, adresati,
        "Lekce09, email s přílohou, ep. II"
    )

    zdroj_html = precti_html_predlohu("index.html")
    text = nahrad_promenne_v_textu(zdroj_html, jmeno="Matouš", lekce="9. lekci")
    email.set_content(text, "html")

    email = pridej_prilohu(email, "lesson09.ipynb")

    with smtplib.SMTP_SSL('smtp.gmail.com', context=context) as smtp:
        smtp.login(odesilatel, os.getenv("demo_password"))  # nezapomeň na heslo
        smtp.sendmail(odesilatel, adresati, email.as_string())


if __name__ == "__main__":
    main()
