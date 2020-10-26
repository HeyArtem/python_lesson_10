

'''
Это тоже глава 10.2 тестирование классов pytest
Сюда мы импортируем игру из Тестирование102классов_Pytest


Артем!!! Запомни сколько ты потерял часов, пока вспомнил, 
что страница должна называться со слова !!!test  тестируемая функция со слова test и в терминале писать слово pytest!!!

'''

import pytest
from Тестирование102классов_Pytest import Dice_incapsulation
# для написания тестов создадим спецю класс

class TestDice: # когда пишем урок incapsulation изменили название класса с TestDice на TestDice_pytest

    def setup(self): # позже обьяснят, для чего эти функции
        ''''
        Зачем setup?
        В каждо функции мы повторяем код
          dice_game = Dice_incapsulation(2)
        что бы не повторять, мы создаем обьект
        dice_game = Dice_incapsulation(2)
        (причем пишем self.dice_game т.к.это атрибут класса class TestDice и везде ниже дапишем слово self.)
         -> в кажд фу-ции удаляем его(до этого в каждой функции была запись dice_game = Dice_incapsulation(2)
        и еще просто запринтим StartTest
        '''
        self.dice_game = Dice_incapsulation(2)
        print('Start test!') # просто так запрнтил


    def teardown(self):
        ''''
        teardown то, что выполняется после завершения тестирования,
        например это может быть удаление обьектов, очистка памяти
        или отключение соединение базы данных с сервреом

        Для примера включю обнуление счетчика бросков current_throw
        '''
        self.dice_game.current_throw == 0
        print('Test has done! Короче закончен')


    def test_init(self): # протестируем init
        assert self.dice_game.throw_num == 2
        ''''
        Тест 1
        ПРотестируем init, убедимся, что когда передаем значеи N,
        параметр throw_num = N
        '''

        assert self.dice_game.current_throw == 0
        ''''
        Тест 2
        тестируем счетчик бросков
        '''


    def test_dice_setter(self):
        ''''
        Тест 3
        Протестируем функцию присваивания через setter
        '''
        self.dice_game.hidden_num_1 = 5
        self.dice_game.hidden_num_2 = 5
        assert (self.dice_game.hidden_num_1 == 5) & (self.dice_game.hidden_num_2 == 5)
        ''''Сложное условие, что первый и второй будут 5 одновременно'''

        with pytest.raises(ValueError):
            ''''
            Тест4
            Спец. ключевое слово, похоже на менеджер контекста
            слово with
            Протестируем фу-ю присваивания которую мы написали с помощью Сетера
            ValueError ошибка которую пытаемся поймать
            Напишем например = 8, это выходит за пределы (dice > 0) & (dice < 7)
            
            !!!  У меня почему то система не выполняет этот тест, не важно какое число стоит !!!
            
            Так же мы можем написать в место ValueError -> TypError и тест будет провален 
            '''
            self.dice_game.hidden_num_1 = 200000 # ну не работает!!

    def test_throw_dices(self):
        '''
        Тест 5
        ПРотестируем функцию throw_dices.
        Убедимся, что счетчик уведичивается с каждым броском
        '''
        self.dice_game.set_hidden_numbers()
        self.dice_game.throw_dices() # это бросили кости
        assert self.dice_game.current_throw == 1






    def test_change_dices(self):
        ''' дописали во время 10.4 coversge(покрытие тастами)'''
        self.dice_game.set_hidden_numbers()
        dice1 = self.dice_game.hidden_num_1
        dice2 = self.dice_game.hidden_num_2

        self.dice_game.change_dices()
        assert {dice1,dice2} != {self.dice_game.hidden_num_1, self.dice_game.hidden_num_2}
















