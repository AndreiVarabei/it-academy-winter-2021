# Проверить, действительно ли введены стороны треугольника и посчитать его площадь

a = int(input("Введите сторону треуголтника a: "))
b = int(input("Введите сторону треуголтника b: "))
c = int(input("Введите сторону треуголтника c: "))
p = (a + b + c) / 2

if a < b + c:
    if b < a + c:
        if c < a + b:
            s = (p * (p - a) * (p - b) * (p - c)) ** (0.5)
            print(" Площадь тругольника равна : ", s )
else:
    print("Невернные данные")
