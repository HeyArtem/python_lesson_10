# скопировал сюда игру в кости из прошлого урока, для новой темы 10.1_polymorfism

import random
class Dice:
    def __init__(self, N):
        self.throw_num = N # Броски
        self.current_throw = 0 # Параметр отвечает за количество совершенных бросков

    def set_hidden_numbers(self):  # настройка параметров бросания костей
        self._hidden_num_1 = random.randint(1,6)  # _'земля' в начале, значит, что параметры скрытые
        self._hidden_num_2 = random.randint(1,6)
        #print("печатаю self._hidden_num 1 и 2: ", self._hidden_num_1, self._hidden_num_2)
        #print("печатаю self._hidden_num 1 и 2: ", self._hidden_num_1, self._hidden_num_2)         # это я мониторю

    def throw_dices(self):
        dice_1 = random.randint(1, 6) # бросаем кости
        dice_2 = random.randint(1, 6) # бросаем кости 2
        self.current_throw+=1
        #print("Печатаю self.current_throw: ", self.current_throw)
        #print("Печатаю dice 1 и 2: ", dice_1, dice_2 )
        if self.current_throw > self.throw_num: # если количество бросков превысило запланированное
        #print("Печатаю self.current_throw: ", self.current_throw)           # это я мониторю
        #print("Печатаю dice 1 и 2: ", dice_1, dice_2 )                      # это я мониторю
            raise Exception("Вы превысили количество попыток! ")

        if {dice_1,dice_2} == {self._hidden_num_1, self._hidden_num_2}: # Почему оформлено, как множество (только уникальные элементы?)
            return True
        else:
            return False

if __name__ == "__main__": # Что это???
    dice_game = Dice(2)
    dice_game.set_hidden_numbers()
    #print(dice_game._hidden_num_1, dice_game._hidden_num_2) # почему обращаемся через dice_game?
    for i in range(4):  # зачем Dice=20 и range=100?
        try:
            print(dice_game.throw_dices())
        except:
            print("Игра закончена")