''''
Изучаю pytest от Эльдара ч.1
Здесь пишу тестируемую функцию
'''

def get_formatted_name(first, last):
    ''''
    Функция, получает имя и фамилию и возвращает
    отформатированное полное имя (первая буква имени и фамилии будет Заглавной
    '''
    full_name = f"{first} {last}"
    return full_name.title()
name_good = get_formatted_name('фЕрДинАНт', 'бЕКкеР')
print(name_good)