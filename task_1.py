# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c -
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не
# существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input('Введите размер стороны a: '))
b = int(input('Введите размер стороны b: '))
c = int(input('Введите размер стороны c: '))

if a >= b + c or b >= a + c or c >= a + b:
    print('Треугольника с такими расмерами не существует.')
elif a == b == c:
    print('Треугольник равносторонний.')
elif a == b or b == c or a == c:
    print('Треугольник равнобедренный')
elif a != b != c:
    print('Треугольник разносторонний')