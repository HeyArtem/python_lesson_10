'''
Это тоже глава 10.2 тестирование классов pytest
Сюда мы импортируем игру из Тестирование102классов_Pytest

'''
from Тестирование102классов_Pytest import Dice_incapsulation
# для написания тестов создадим спецю класс

class testDice:

    def setup(self): # позже обьяснят, для чего эти функции
        pass

    def teardown(self): # позже обьяснят, для чего эти функции
        pass


    def test_init(self): # протестируем init
        dice_game = Dice_incapsulation(2) # тестируем self.throw_num = N # Броски
        assert dice_game.throw_num == 2
        assert dice_game.current_throw == 0

        # протестируем self.current_throw = 0 что текущих бросков 0

