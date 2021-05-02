#Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 —
#получаем «5 процентов», задаем число 2 — получаем «2 процента». Вывести все склонения
#для проверки.
#Как красиво написать список с форматами я не разобрался пока что
percent_input = int(input('Введите число процентов: '))
percent_name = ('процентов','процент','процента')

if 0 <= percent_input < 1 or percent_input >= 5:
    print(percent_input, percent_name[0])
elif percent_input == 1:
    print(percent_input, percent_name[1])
elif 1 < percent_input <= 4:
    print(percent_input, percent_name[2])

percent = 0
percent_list = []

while percent <= 20:
    if 0 <= percent < 1 or percent >= 5:
        percent_number = (percent, percent_name[0])
    elif percent == 1:
        percent_number = (percent, percent_name[1])
    elif 1 < percent <= 4:
        percent_number = (percent, percent_name[2])
    percent_list.append(percent_number)
    percent += 1

print(percent_list)