import unittest
from name_function import get_formatted_name # импортируем тестируемую функцию из странички name_function

''''
Изучаю pytest от Эльдара ч.3

Прохождение теста
Чтобы написать тестовый сценарий для функции, импортируем модуль unittest и функцию, 
которую необходимо протестировать. 
Затем создадим класс, наследующий от unittest.
TestCase, и напишем серию методов для тестирования различных аспектов поведения данной функции.

Ниже приведен тестовый сценарий с одним методом, который проверяет, 
что функция get_formatted_name() правильно работает при передаче имени и фамилии. 


Оф.сайт:
https://docs.python.org/3/library/unittest.html#
'''

class NamesTestCase(unittest.TestCase):
    ''''
    Тесты для 'name_function.py'.
    класс должен наследовать от класса unittest.TestCase,
    чтобы Python знал, как запускать написанные тесты
    '''

    def test_метод_проверка_имени(self):
        ''''
        Этот метод будет тестировать один аспект, а именно
        делает ли функция get_formatted_name форматирование
        (первые буквы заглавные, остальные строчные)
        Обязательно имя метода должно начинаться со слова test !!
        '''

        имя_по_формату = get_formatted_name('зиНА', 'дуБАлоМОВА')
        ''''
        Вызываем тестируемую функцию get_formatted_name и сохраняем 
        возвращаемое значение, в переменной 'имя_по_формату' 
        для дальнейшей проверки
        '''
        self.assertEqual(имя_по_формату, 'Зина Дубаломова ')
        ''''
        метод assertEqual(a, b) проверяет, что a==b
        т.е. 'имя_по_формату (мы его пропустили через функцию форматирования)'
        равно 'Здесь мы вручную прописали как должно быть правильно прописано имя'
        т.е. 'зиНА дуБАлоМОВА' будет написано 'Зина Дубаломова'
        '''
    def test_first_last_middle_name(self):
        ''''
        Добавил этот метод для главы добавление новых тестов (дальше)
        Будем тестировать что функция работает не только для имени и фамилии,
        но и может работать с данными содержащими имя, фамилию и отчество'''
        имя_по_формату = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(имя_по_формату, 'Wolfgang Mozart Amadeus')

'''' 
Метод 
test_метод_проверка_имени() 
будет выполняться автоматически при запуске test_name_function.py, т.к. начинается с test_.'''

if __name__ == '__main__':
        unittest.main()
        ''''
        Многие тестовые фреймворки импортируют тестовые файлы перед их выполнением. 
        При импортировании файла интерпретатор выполняет файл в процессе импортирования. 
        В этом случае специальная переменная 
        __name__ содержит имя модуля (файла без расширения). 
        Прямой запуск программы присваивает специальной переменной 
        __name__ значение '__main__', 
        указывая на то, что файл выполняется как главная программа. 
        В этом случае вызывается метод unittest.main(), который выполняет тестовый сценарий.
        '''

''''
После запуска мы увидим:
 '.' точку (количество точек соответствует количеству тестов)
 '---' пунктирную строку
 'Ran 1 test in 0.000s'
 'OK' 
 '''


''''
Сбой теста
Изменим функцию get_formatted_name(), чтобы она работала с вторыми именами. 
Сделаем это так, чтобы она перестала работать с полными именами из двух компонентов. 
Заменим содержимое файла name_function.py

Запустим и увидим инфо о ошибке:
Тестирование показывает, что она перестала работать для полных имен из двух компонентов.

При сбое информации больше, поскольку разработчику необходимо разобраться в причинах сбоя.

* E - свидетельствует о том, что один модульный тест в тестовом сценарии привел к ошибке.

* После слова ERROR указывается имя теста, в котором произошла ошибка (в тесте test_first_last_name() в NamesTestCase).

*После слова Traceback раскрывается причина сбоя (вызов функции get_formatted_name('janis', 'joplin') перестал работать из-за необходимого позиционного аргумента).

*В строке со словом Ran указано, что был выполнен один модульный тест в указанное время.

*FAILED - информирует, что тестовый сценарий в целом не прошел; (errors=1) - в ходе выполнения произошла одна ошибка при выполнении тестового сценария.

'''


''''
Добавление новых тестов

ля того, чтобы гаранировать выполнение данной функции для имен из трех компонентов 
напишем еще один тест.
Добавим в класс NamesTestCase следующий 
метод test_first_last_middle_name():
'''

