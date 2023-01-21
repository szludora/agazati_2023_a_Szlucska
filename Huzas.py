class Huzas:
    def __init__(self, azonosito, ev, het, a, b, c, d, e, f):
        self.azonosito = azonosito
        self.ev = ev
        self.het = het
        self.lista = []
        self.lista.append(int(a))
        self.lista.append(int(b))
        self.lista.append(int(c))
        self.lista.append(int(d))
        self.lista.append(int(e))
        self.lista.append(int(f))

    def __str__(self):
        return f"{self.lista}"
