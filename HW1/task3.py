# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу
# и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_LIMIT = 0
MAX_LIMIT = 100000
UNITY = 1
MIN_PRIME_NUM = 2

num = -1

while not (MIN_LIMIT <= num <= MAX_LIMIT):
    num = int(input(f"Введите целое число между {MIN_LIMIT} и {MAX_LIMIT} : "))
if num >= MIN_PRIME_NUM:
    sum = 0
    for i in range(UNITY, num + 1):
        if num % i == 0:
            sum += 1
    if sum <= 2:
        print(f"Число {num} простое")
    else:
        print(f"Число {num} составное")
else:
    print("Числа 0 и 1 не являются ни простыми, ни составными")