''''
Изучаю pytest от Эльдара ч.1
Здесь пишу тестируемую функцию
'''

# def get_formatted_name(first, last):
#     ''''
#     Функция, получает имя и фамилию и возвращает
#     отформатированное полное имя (первая буква имени и фамилии будет Заглавной
#     '''
#     full_name = f"{first} {last}"
#     return full_name.title()

# name_good = get_formatted_name('фЕрДинАНт', 'бЕКкеР')
# print(name_good)

''''
Сбой теста
(ч.3 стр test_name_function)

Изменим функцию get_formatted_name(), чтобы она работала с вторыми именами. 
Сделаем это так, чтобы она перестала работать с полными именами из двух компонентов. 
Заменим содержимое файла name_function.py следующим кодом:
'''
def get_formatted_name(first, middle, last=''):
    """
    Строит отформатированное полное имя.
    Эта версия должна работать для полных имен из трех компонентов.
    """
    if middle:
        full_name = f"{first} {middle} {last}" # добавили второе имя
    else:
        full_name = f"{first}{last}"
    return full_name.title()

# name_2_good = get_formatted_name('соНЯ', 'заБИЯкИНА', 'влаДИмирОВна')
# print(name_2_good)
#
# name_3_good = get_formatted_name('фЕрДинАНт', 'бЕКкеР')
# print(name_3_good)

