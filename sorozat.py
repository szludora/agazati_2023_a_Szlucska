import random


def general():
    szamok = []
    while len(szamok) < 8:
        vel = int(random.random()*960) - 100
        szamok.append(vel)

    kiir = ""
    i = 0
    while i < len(szamok):
        if i == len(szamok) - 1:
            kiir += str(szamok[i])
        else:
            kiir += str(szamok[i]) + "; "
        i += 1
    print("II/A, B, C:")
    print("\t", kiir, "\n")

    konzol_ir(szamok)


def tizzel_oszthatoak_szama(szamok):
    i = 0
    db = 0
    while i < len(szamok):
        if szamok[i] % 10 == 0:
            db += 1
        i += 1

    return db


def konzol_ir(szamok):
    db = tizzel_oszthatoak_szama(szamok)
    print("II/D, E:")
    print("\tTízzel osztható számok száma: ", db, "\n")

    fajlba_ir(db)


def fajlba_ir(eredmeny):
    fajl = open("vegeredmeny.txt", "w", encoding="utf-8")
    fajl.write(str(eredmeny))
    fajl.close()
