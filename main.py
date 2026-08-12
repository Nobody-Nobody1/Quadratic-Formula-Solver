from pyquadratic.pyquadratic import *

def check_sign(value):
    if value > 0:
        values.append("+")

if __name__ == "__main__":
    values = []
    a = int(input("Enter value for a: "))
    values.append(a)
    values.append("x^2")
    b = int(input("Enter value for b: "))
    check_sign(b)
    values.append(b)
    values.append("x")
    c = int(input("Enter value for c: "))
    check_sign(c)
    values.append(c)
    result = ''.join(str(x) for x in values)
    print(result)
    print(realSolution(result))