from Polynom import *
print("Polynome:")
p1 = Polynom([3, 0, 4, -6, 0, 12])
p2 = Polynom([0, 2, -7])
x1 = 2
x2 = 5
print("p1:",p1)
print("p2:",p2)
print()
print("Grad von Polynom p1:",p1.grad())
print("Grad von Polynom p2:",p2.grad())
print("p1 gleich p2?", p1 == p2)
print("Muplitplikation von p1 mit p2:", p1 * p2)
print("Addition von p1 mit p2:", p1 + p2)
print("Auswertung von p1 für x =",x1,":", p1.auswerten(x1))
print("Auswertung von p2 für x =",x2,":", p2.auswerten(x2))