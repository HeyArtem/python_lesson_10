''''
10.3 unittest
В юниттесте есть такие  же функции аналог, как в пайтесте setup и teardown

 setup будет всегда выполняться при каждом запуске теста написанного далее
'''

import unittest
from incapsulation import Dice_incapsulation

class TestDice_unittest(unittest.TestCase):
    '''
    unittest.TestCase это мы унаследовались от юнитеста
    и тогда появяться различные функции типа self.assertEqual
    или self.assertFalse(проверяет является ли выражение ложным)
    '''
    def setUp(self):
        print('Start test !')
        self.dice_game = Dice_incapsulation(3)
        self.dice_game.set_hidden_numbers()

    def tearDown(self):
        self.dice_game.current_throw = 0
        print('Test completed!')
        del self.dice_game # Обычно происходит освобождение кэша. дописали позже.

    def test_init(self):
        '''
        мы скопировали класс из test_pytest_dices, но в юнитесте нужно заменить,
        конкретно на функцию сравнения
        assert на self.assertEqual и перечислим параметры
        и assert на self.assertFalse
        '''
        self.assertEqual(self.dice_game.throw_num, 3)
        self.assertFalse(self.dice_game.current_throw > 0)

    def test_dice_setter(self):
        self.dice_game.hidden_num_1 = 5
        self.dice_game.hidden_num_2 = 5
        self.assertTrue((self.dice_game.hidden_num_1 == 5)&(self.dice_game.hidden_num_2 == 5))
        '''
        скопировали и заменяем assert на self.assertTrue  
        '''

        with self.assertRaises(ValueError):
            '''
            скопировали и заменяем pytest.raises на self.assertRaises
            '''
            # код вызывающий данную ошибку
            self.dice_game.hidden_num_1 = 8
            '''
            происходит некоторый код, который должен вызвать ошибку ValueError
            и если это она, то тогда не будет ассерта, а если не она, то будет ассерт
            '''

