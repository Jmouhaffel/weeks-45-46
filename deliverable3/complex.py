class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        sign = "+" if self.im >= 0 else ""
        return f"{self.re}{sign}{self.im}i"

    def __repr__(self):
        return f"Complex({self.re}, {self.im})"

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re - other, self.im)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other - self.re, -self.im)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real = self.re * other.re - self.im * other.im
            imag = self.re * other.im + self.im * other.re
            return Complex(real, imag)
        elif isinstance(other, (int, float)):
            return Complex(self.re * other, self.im * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.re == other.re and self.im == other.im
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
