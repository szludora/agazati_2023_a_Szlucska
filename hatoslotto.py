from Huzas import Huzas


def feladat():
    fajl = open("hatos.csv", "r", encoding="utf-8")
    fejlec = fajl.readline()
    sorok = fajl.readlines()
    fajl.close()

    huzasok = []
    ossz = 0
    db = 0
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("@")
        huzas = Huzas(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5], sor[6], sor[7], sor[8])
        """42 héten történő húzások összeadása"""
        if huzas.het == "42":
            ossz += huzas.lista[0] + huzas.lista[1] + huzas.lista[2] + \
                     huzas.lista[3] + huzas.lista[4] + huzas.lista[5]
            db += 1
        huzasok.append(huzas)
        i += 1

    """az összeadott számokat elosztom a 42 héten történt összes tipp leadott darabszámával"""
    atlag = ossz / (db * 6)

    print("III/A, B:")
    print("\tA húzások száma:", len(huzasok))
    print("III/C:")
    print(f"\tA 42 héten húzott számok átlaga: {atlag:.2f}")
    print("III/D:")
    print("\tA legnagyobb kihúzott szám értéke: nem megállapítható")
