# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.
# c. * Решить задачу под пунктом b, не создавая новый список

number = 1
cube_list = []

while number <= 1000:
    if number % 2:
        cube_number = number ** 3
        cube_list.append(cube_number)
        number += 1
    else:
        number += 1

total_sum = 0

for number_digit_sum_divisible_by_7 in cube_list:
    number_sum = 0
    number_check = number_digit_sum_divisible_by_7
    while number_check != 0:
        digit = number_check % 10
        number_sum += digit
        number_check = number_check // 10
    if not number_sum % 7:
        total_sum += number_digit_sum_divisible_by_7

print('Список, состоящий из кубов нечётных чисел от 1 до 1000 -', cube_list)

idx = 0
number_sum_plus_17 = 17
total_sum_plus_17 = 0

for idx in range(len(cube_list)):
    cube_list[idx] += number_sum_plus_17
for number_digit_sum_divisible_by_7 in cube_list:
    number_sum = 0
    number_check = number_digit_sum_divisible_by_7
    while number_check != 0:
        digit = number_check % 10
        number_sum += digit
        number_check = number_check // 10
    if not number_sum % 7:
        total_sum_plus_17 += number_digit_sum_divisible_by_7

print('Сумма значений кубов нечётных чисел, сумма цифр которых делится на 7 = ', total_sum)
print('Сумма значений кубов нечётных чисел, к каждому из которых прибавили 17, и сумма цифр которых делится на 7 = ', total_sum_plus_17)