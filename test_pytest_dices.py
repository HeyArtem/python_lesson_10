import pytest

'''
Это тоже глава 10.2 тестирование классов pytest
Сюда мы импортируем игру из Тестирование102классов_Pytest


Артем!!! Запомни сколько ты потерял часов, пока вспомнил, 
что страница должна называться со слова test

'''


from Тестирование102классов_Pytest import Dice_incapsulation
# для написания тестов создадим спецю класс

class TestDice_pytest: # когда пишем урок incapsulation изменили название класса с TestDice на TestDice_pytest

    def setup(self): # позже обьяснят, для чего эти функции

        '''
        Так, как в каждой функции идет дублирование кода
        например:
        dice_game = Dice_incapsulation(2)

        Мы создали объект self.dice_game, который является атрибутом класса setup
        Теперь во всем коде мы можем обращаться к обьекту dice_game через атрибут self.dice_game


        '''
        self.dice_game = Dice_incapsulation(3)
        print('Start test!') # просто так запрнтил

    def teardown(self): # teardown то, что выполняется после завершения
        self.dice_game.current_throw = 0 # мы можем например, каждый раз обновлять current_throw
        print('Test has done!')


    def test_init(self): # протестируем init
        # dice_game = Dice_incapsulation(2) # тестируем self.throw_num = N  Броски. Закоментил, т.к. использую def setup
        assert self.dice_game.throw_num == 3
        assert self.dice_game.current_throw == 0 # текущий бросок

    def test_dice_setter(self):
        # dice_game = Dice_incapsulation(3) #Закоментил, т.к. использую def setup
        self.dice_game.hidden_num_1 = 5
        self.dice_game.hidden_num_2 = 5
        assert (self.dice_game.hidden_num_1 == 5) & (self.dice_game.hidden_num_2 == 5)


        with pytest.raises(ValueError):
            # код вызывающий данную ошибку
            self.dice_game.hidden_num_1 = 8

    def test_throw_dices(self):
        # dice_game = Dice_incapsulation(3) Закоментил, т.к. использую def setup
        self.dice_game.set_hidden_numbers()
        self.dice_game.throw_dices()
        assert self.dice_game.current_throw == 1



