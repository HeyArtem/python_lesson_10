# 10.1 Polymorfism. Скопирую игру в кости из прошлого урока.


# Разобраться самому, препод сказал сами посмотрите и я забыл как работает механика игры

from dice_game import Dice
''''
Сделаем несколько полиморфных от класса Dice
Будем создавать классы с разным типом игры

Поменяем только одну функцию - функцию бросания type_1

'''

class Dice_type_1(Dice):
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

        if {dice_1 + dice_2} == {self._hidden_num_1 + self._hidden_num_2}: # МЫ сделали, если сумма выпавших, совпадает с загаданным
            return True
        else:
            return False


''''
Создадим type_2

'''

class Dice_type_2(Dice):
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
        if (dice_1 in {self._hidden_num_1, self._hidden_num_2}) or (dice_2 in {self._hidden_num_1, self._hidden_num_2}): # Новое условие

            return True
        else:
            return False













if __name__ == '__main__':
    game = Dice(3)
    print(type(game)) # посмотрим типы созданных обьектов

    game_type_1 = Dice_type_1(5)
    print(type(game_type_1))

    game_type_2 = Dice_type_2(5)
    print(type(game_type_2))