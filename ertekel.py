def ertekeles():
    nap = input("Hét napja: ")
    ora = input("Óra neve: ")
    jegy = int(input("Értékelés (1-5): "))

    while jegy > 5 or jegy < 1:
        if jegy < 0:
            jegy = int(input("Az értékelés nem lehet negatív!"))
        elif jegy == 0:
            jegy = int(input("Az értékelés nem lehet 0!"))
        elif jegy > 5:
            jegy = int(input("5 pont feletti értékelés nem elfogadható!"))

    print("I/A, B: ")
    print("\tHét napja:", nap, "\n\tÓra neve:", ora, "\n\tÉrtékelés (1-5):", jegy)
    print("Köszönjük az értékelést!\n")
