import math

class Punto:
    def _init_(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return (self.x, self.y)

    def coord_polares(self):
        r = math.sqrt(self.x*2 + self.y*2)
        theta = math.atan2(self.y, self.x)
        return (r, math.degrees(theta))

    def _str_(self):
        return f"Punto({self.x}, {self.y})"


class Linea:
    def _init_(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2

    def _str_(self):
        return f"Linea({self.p1}, {self.p2})"

    def dibuja_linea(self):
        return f"Dibujo línea desde {self.p1} hasta {self.p2}"


class Circulo:
    def _init_(self, centro: Punto, radio: float):
        self.centro = centro
        self.radio = radio

    def _str_(self):
        return f"Circulo(Centro: {self.centro}, Radio: {self.radio})"

    def dibuja_circulo(self):
        return f"Dibujo círculo con centro en {self.centro} y radio {self.radio}"


# Ejemplo 
p1 = Punto(3, 4)
p2 = Punto(6, 8)
linea = Linea(p1, p2)
circulo = Circulo(p1, 5)

print(p1)
print(p1.coord_cartesianas())
print(p1.coord_polares())

print(linea)
print(linea.dibuja_linea())

print(circulo)
print(circulo.dibuja_circulo())