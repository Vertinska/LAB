X = float(input("Введите длину стороны X: "))
Y = float(input("Введите длину стороны Y: "))
Z = float(input("Введите длину стороны Z: "))
T = float(input("Введите длину стороны T: "))

def area_of_triangle1(a, b):
    return (a * b) / 2

def area_of_triangle2(a, b, c):
    p=(a+b+c)/2
    area=pow(p*(p-a)*(p-b)*(p-c),0.5)
    return area

final=area_of_triangle1(X, Y)+area_of_triangle2(Z, T, pow(X*X+Y*Y,0.5))
print(f"Площадь четырехугольника: {final:.2f}")



def term_n(a1, d, n):
    if n == 1:
        return a1
    else:
        return term_n(a1, d, n - 1) + d


a1 = float(input("Введите первый член прогрессии: "))
d = float(input("Введите разность прогрессии: "))
n = int(input("Введите номер члена прогрессии: "))


nth_term = term_n(a1, d, n)

print(f"n-й член арифметической прогрессии: {nth_term}")
