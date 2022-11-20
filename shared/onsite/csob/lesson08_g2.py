import string
from random import choices  # random -> random.choices


def vrat_ciselne_znaky(prepinac: bool):
    if prepinac:
        return string.digits
    else:
        return ""


def vrat_male_textove_znaky(prepinac: bool):
    if prepinac:
        return string.ascii_lowercase
    else:
        return ""


def vrat_velke_textove_znaky(prepinac: bool):
    if prepinac:
        return string.ascii_uppercase
    else:
        return ""


def vytvor_captcha(pole_znaku: str, delka: int):
    return "".join(choices(pole_znaku, k=delka))


def main():
    print(
        vytvor_captcha(
            "".join(
                (
                    vrat_ciselne_znaky(True),         # str
                    vrat_male_textove_znaky(False),   # str
                    vrat_velke_textove_znaky(True),   # str
                )
            ),  # "abcABC123"
            delka=7)
    )


if __name__ == "__main__":
    main()
