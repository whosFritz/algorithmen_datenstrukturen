class Polynom:
    def __init__(self, koeffizienten):
        self.koeffizienten = koeffizienten

    def grad(self):
        return len(self.koeffizienten) - 1

    def __eq__(self, other):
        return self.koeffizienten == other.koeffizienten

    def __add__(self, other):
        max_grad = max(self.grad(), other.grad())
        self_koeffizienten = self.koeffizienten + [0] * (max_grad - self.grad())
        other_koeffizienten = other.koeffizienten + [0] * (max_grad - other.grad())
        ergebnis_koeffizienten = [0] * (max_grad + 1)
        for i in range(max_grad + 1):
            ergebnis_koeffizienten[i] = self_koeffizienten[i] + other_koeffizienten[i]
        return Polynom(ergebnis_koeffizienten)

    def __mul__(self, other):
        ergebnis_koeffizienten = [0] * (self.grad() + other.grad() + 1)
        for i in range(self.grad() + 1):
            for j in range(other.grad() + 1):
                ergebnis_koeffizienten[i + j] += self.koeffizienten[i] * other.koeffizienten[j]
        return Polynom(ergebnis_koeffizienten)

    def auswerten(self, x):
        ergebniss = 0
        for i in range(self.grad() + 1):
            ergebniss += self.koeffizienten[i] * x ** i
        return ergebniss
    
    def __str__(self):
        ergebnis = ""
        for i, koeffizient in enumerate(self.koeffizienten):
            if koeffizient == 0:
                continue
            if koeffizient < 0:
                ergebnis += " - "
            else:
                if i > 0 or (i == 0 and koeffizient != 1):
                    ergebnis += " + "
            if abs(koeffizient) != 1 or i == 0:
                ergebnis += str(abs(koeffizient))
            if i > 0:
                ergebnis += "x"
                if i > 1:
                    ergebnis += "^" + str(i)
        return ergebnis
