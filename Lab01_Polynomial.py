class Term:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power


class Polynomial:
    def __init__(self):
        self.x = []

    def addTerm(self, coeff, power):
        self.x.append(Term(coeff, power))

    def get_degree(self):
        maxi = 0
        for i in self.x:
            if i.power > maxi:
                maxi = i.power
        return f"Degree of polynomial is {maxi}"

    def get_coeff(self, power):
        for i in self.x:
            if i.power == power:
                return i.coeff

    def evaluate(self, value):
        a = 0
        for i in self.x:
            a += (value ** i.power) * i.coeff
        return a

    def add_polynomial(self, other):
        result = Polynomial()
        list_i = []
        list_j = []
        for i in range(len(self.x)):
            for j in range(len(other.x)):
                if self.x[i].power == other.x[j].power:
                    result.addTerm(self.x[i].coeff + other.x[j].coeff, self.x[i].power)
                    list_i.append(i)
                    list_j.append(j)
        for i in range(len(self.x)):
            if i not in list_i:
                result.addTerm(self.x[i].coeff , self.x[i].power)
        for i in range(len(other.x)):
            if i not in list_j:
                result.addTerm(other.x[i].coeff , other.x[i].power)
        return result

    def derivative(self):
        result = Polynomial()
        for i in self.x:
            if i.power != 0:
                result.addTerm(i.coeff * i.power, i.power - 1)
        return result

    def antideri(self):
        result = Polynomial()
        for i in self.x:
            if i.power == 0:
                result.addTerm(i.coeff, 1)
            else:
                result.addTerm((i.coeff / i.power + 1), (i.power + 1))
        return result

    def addtocoeff(self, coefff, powerr):
        result = Polynomial()
        for i in self.x:
            if i.power == powerr:
                result.addTerm((i.coeff + coefff), i.power)
            else:
                result.addTerm(i.coeff, i.power)
        return result

    def clear(self):
        result = Polynomial()
        for i in self.x:
            result.addTerm(0, i.power)
        return result

    def newcoeff(self, new, power):
        result = Polynomial()
        a = 0
        for i in self.x:
            if i.power == power:
                result.addTerm(new, i.power)
                a = 1
            else:
                result.addTerm(i.coeff, i.power)
        if a == 0:
            result.addTerm(new, power)
        return result

    def mul(self, other):
        result = Polynomial()
        for i in self.x:
            for j in other.x:
                result.addTerm(i.coeff * j.coeff, i.power + j.power)
        return result

    def sub (self,other):
        result = Polynomial()
        list_i = []
        list_j = []
        for i in range(len(self.x)):
            for j in range(len(other.x)):
                if self.x[i].power == other.x[j].power:
                    result.addTerm(self.x[i].coeff - other.x[j].coeff, self.x[i].power)
                    list_i.append(i)
                    list_j.append(j)
        for i in range(len(self.x)):
            if i not in list_i:
                result.addTerm(self.x[i].coeff , self.x[i].power)
        for i in range(len(other.x)):
            if i not in list_j:
                result.addTerm(-1*other.x[i].coeff , other.x[i].power)
        return result


    def __str__(self):
        string = ""
        for i in range(len(self.x)):
            string += f" {self.x[i].coeff}x^{self.x[i].power} "
            if i != len(self.x)-1:
                string += "+"
        return string


def main():
    p1 = Polynomial()
    p1.addTerm(4, 5)
    p1.addTerm(7, 3)
    p1.addTerm(-1, 2)
    p1.addTerm(9, 0)
    p2 = Polynomial()
    p2.addTerm(6, 4)
    p2.addTerm(3, 2)
    p2.addTerm(2, 1)
    print("P1: ", p1)
    print("P2: ", p2)
    print(p1.evaluate(2))
    print(p2.evaluate(2))
    print("Addition Result:")
    print(p1.add_polynomial(p2))
    print("Derivative Result:")
    print(p1.derivative())
    print("Anti Derivative")
    print(p1.antideri())
    print(p1.addtocoeff(3, 2))
    print(p1.clear())
    print(p1.newcoeff(2, 5))
    print("Multiplication")
    print(p1.mul(p2))
    print('Subtraction Result')
    print(p1.sub(p2))


main()
