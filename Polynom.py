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
        erg_koeffizienten = [0] * (max_grad + 1)
        for i in range(max_grad + 1):
            erg_koeffizienten[i] = self_koeffizienten[i] + other_koeffizienten[i]
        return Polynom(erg_koeffizienten)

    def __mul__(self, other):
        erg_koeffizienten = [0] * (self.grad() + other.grad() + 1)
        for i in range(self.grad() + 1):
            for j in range(other.grad() + 1):
                erg_koeffizienten[i + j] += self.koeffizienten[i] * other.koeffizienten[j]
        return Polynom(erg_koeffizienten)

    def auswerten(self, x):
        erg = 0
        for i in range(self.grad() + 1):
            erg += self.koeffizienten[i] * x ** i
        return erg
    
    def __str__(self):
        erg = ""
        for i, koeffizient in enumerate(self.koeffizienten):
            if koeffizient == 0:
                continue
            if koeffizient < 0:
                erg += " - "
            else:
                if i > 0 or (i == 0 and koeffizient != 1):
                    erg += " + "
            if abs(koeffizient) != 1 or i == 0:
                erg += str(abs(koeffizient))
            if i > 0:
                erg += "x"
                if i > 1:
                    erg += "^" + str(i)
        return erg
