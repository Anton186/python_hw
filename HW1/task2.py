# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.

print("Введите стороны треугольника: ")
a, b, c = float(input("a = ")), float(input("b = ")), float(input("c = "))
if a < b + c and b < a + c and c < a + b:
    print("Треугольник существует")
    if a == b == c:
        print("Этот треугольник равносторонний")
    elif a == b or b == c or a ==c:
        print("Этот треугольник равнобедренный")
    else:
        print("Этот треугольник разносторонний")
else:
    print("Такой треугольник не может существовать")