from abc import ABC, abstractmethod
import math


class Figura(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def pole(self):
        pass

class Prostokat(Figura):
    def __init__(self, wysokosc: int, szerokosc: int):
        # super().__init__()
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc

    def pole(self):
        return self.wysokosc * self.szerokosc

class Kolo(Figura):
    def __init__(self, promien):
        # super().__init__()
        self.promien = promien
    @property
    def pole(self):
        return (math.pi)*(self.promien)**2
    

p1 = Prostokat(10, 15)
p2 = Prostokat(8, 10)
k1 = Kolo(5)
k2 = Kolo(3)

print (f"{p1.pole()} {p2.pole()} {k1.pole:.2F} {k2.pole:.2F}")