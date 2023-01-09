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
        result_koeffizienten = [0] * (max_grad + 1)
        for i in range(max_grad + 1):
            result_koeffizienten[i] = self_koeffizienten[i] + other_koeffizienten[i]
        return Polynom(result_koeffizienten)

    def __mul__(self, other):
        result_koeffizienten = [0] * (self.grad() + other.grad() + 1)
        for i in range(self.grad() + 1):
            for j in range(other.grad() + 1):
                result_koeffizienten[i + j] += self.koeffizienten[i] * other.koeffizienten[j]
        return Polynom(result_koeffizienten)

    def auswerten(self, x):
        result = 0
        for i in range(self.grad() + 1):
            result += self.koeffizienten[i] * x ** i
        return result
    
    def __str__(self):
        result = ""
        for i, koeffizient in enumerate(self.koeffizienten):
            if koeffizient == 0:
                continue
            if koeffizient < 0:
                result += " - "
            else:
                if i > 0 or (i == 0 and koeffizient != 1):
                    result += " + "
            if abs(koeffizient) != 1 or i == 0:
                result += str(abs(koeffizient))
            if i > 0:
                result += "x"
                if i > 1:
                    result += "^" + str(i)
        return result
