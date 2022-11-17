"""
byt0001,55m2,Olomouc,ul.Heyrovského,
byt0003,65m2,Olomouc,ul.Novosadský_dvůr,
"""


def preved_oznaceni_bytu(zaznam: str, vzor: dict) -> str:
    """
    Vrať textový řetězec, který obsahuje převedené označení bytu.
    """
    oznaceni_bytu, *zbytek_dat = zaznam.split(",")[:-1]
    return ",".join((vzor.get(oznaceni_bytu, "neznámý_typ"), *zbytek_dat))


if __name__ == "__main__":
    vzor = {
        "byt0001": "1+1",
        "byt0002": "2+1",
        "byt0003": "2+kk",
        "byt0004": "3+1",
        "byt0005": "3+kk",
        "byt0006": "4+1",
        "byt0007": "4+kk",
    }

    print(
        preved_oznaceni_bytu("byt0009,65m2,Olomouc,ul.Novosadský_dvůr,", vzor),
        preved_oznaceni_bytu("byt0001,55m2,Olomouc,ul.Heyrovského,", vzor),
        sep="\n"
    )
