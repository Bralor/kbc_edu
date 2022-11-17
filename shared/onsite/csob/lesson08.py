import string
import random


def vrat_ciselne_znaky(potreba_cisel: bool) -> str:
    if potreba_cisel:
        return string.digits  # "0123..."
    else:
        return ""


def vrat_male_textove_znaky(potreba_male: bool) -> str:
    if potreba_male:
        return string.ascii_lowercase  # "abcd..."
    else:
        return ""


def vrat_velke_textove_znaky(potreba_velke: bool) -> str:
    if potreba_velke:
        return string.ascii_uppercase  # "ABCD..."
    else:
        return ""


def vytvor_captchu(dostupne_znaky: str, delka: int) -> str:
    return "".join(random.choices(dostupne_znaky, k=delka))


def main():
    print(vytvor_captchu("".join(
            (vrat_ciselne_znaky(True),         # "0123" / ""
            vrat_male_textove_znaky(True),     # "abcd" / "" -> "0123abcdABCD"
            vrat_velke_textove_znaky(False))   # "ABCD" / ""
                ),
            5
        )
    )


if __name__ == "__main__":
    main()
