# Ответ на вопрос о возможности проверки сразу нескольких значений продолжительности: считаю, что список и правда мог бы облегчить задачу. Соответственно, я бы задал его следующим образом:
# duration = [3700, 86400, ... ], затем условие проверки бы задал индекс для каждого элемента idx = 0 и через enumerate в списке for duration_number in duration
# оставил бы текущий вариант проверки с добавлением условия в каждом условном блоке idx += 1. Но у меня так не получилось сделать на практике.
# Возможный вариант проверки нескольких условий - создание функции с условием, что выполнение программы остановится после ввода "quit" в переменную duration

# Первый вариант решения был с переменными, второй просто с print одной строкой. Нужен ли был вариант, предусматривающий нецелое число секунд?
duration = int(input('Введите продолжительность временного отрезка в секундах для проверки: '))

if duration < 0:
    print('Тут вам не Интерстеллар')
elif 0 <= duration < 60:
    is_second = duration % 60
    print(is_second , 'сек')
elif 60 <= duration < 3600:
    is_minute = duration // 60
    is_second = duration % 60
    print(is_minute, 'мин', is_second, 'сек')
elif 3600 <= duration < 86400:
    is_hour = duration // 3600
    is_minute = duration % 3600 // 60
    is_second = duration % 60
    print(is_hour, 'час', is_minute, 'мин', is_second, 'сек')
else:
    is_day = duration // 86400
    is_hour = duration % 86400 // 3600
    is_minute = duration % 86400 % 3600 // 60
    is_second = duration % 60
    print(is_day, 'дн', is_hour, 'час', is_minute, 'мин', is_second, 'сек')
