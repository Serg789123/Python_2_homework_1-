# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше”
# или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 1
n_max = UPPER_LIMIT
n_min = LOWER_LIMIT

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(1, 11):
    n = int(input(f'Попытка № {count}. Угадайте число от 0 до 1000: '))
    if n == num:
        print(f'Число {n} угадано с {count} попытки.')
        quit()
    elif n < num:
        print(f'Введите среднеарифметическое между {n} и {n_max}: ')
        n_min = n
    elif n > num:
        print(f'Введите среднеарифметическое между {n} и {n_min}: ')
        n_max = n
    count += 1
print('Game over :(')
