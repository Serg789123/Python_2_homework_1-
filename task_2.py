# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч

n = int(input('Введите число от 1 до 100000: '))
count = 0

while n < 1 or n > 100000:
    n = int(input('Число введено неверно, введите число от 1 до 100000: '))

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

print('Число является простым' if count == 2 else 'Число составное')
