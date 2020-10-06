# 10.1_2_incapsulation Инкапсуляция

''''
Скопировал сюда игру Dice
Инкапсу-ия будет в том, что я скрою параметр  hidden_num_1 и hidden_num_2


Добавлю функцию: сменить загаданные числа  def change_dices(self):

'''

import random
class Dice_incapsulation:
    def __init__(self, N):
        self.throw_num = N # Броски
        self.current_throw = 0 # Параметр отвечает за количество совершенных бросков

    def set_hidden_numbers(self):  # настройка параметров бросания костей
        self.__hidden_num_1 = random.randint(1,6)  # __ две земли, это значит, что параметры скрыты
        self.__hidden_num_2 = random.randint(1,6)
        #print("печатаю self._hidden_num 1 и 2: ", self._hidden_num_1, self._hidden_num_2)
        #print("печатаю self._hidden_num 1 и 2: ", self._hidden_num_1, self._hidden_num_2)         # это я мониторю



    def change_dices(self):  # новые классы
        self.__hidden_num_1 = random.randint(1, 6)
        self.__hidden_num_2 = random.randint(1, 6)

    def set_dice1(self, dice): # вручную буду менть значения
        #if (dice > 0) & (dice < 7) # мы зачем то это написали но реализовывать не будем
        self.__hidden_num_1 = dice

    def get_dice1(self):
        #if (dice > 0) & (dice < 7)
        return self.__hidden_num_1



    @property
    def hidden_num_1(self):  # что то какой то пипец, третий наворт, я уже потерялся и обвесим ее еще декоратором
        #if (dice > 0) & (dice < 7)
        return self.__hidden_num_1 # теперь мы можем обращаться к скрытой переменной __hidden_num_1, как к hidden_num_1 просто без всего

    @hidden_num_1.setter
    def hidden_num_1(self, dice):
        self.__hidden_num_1 = dice


    @property
    def hidden_num_2(self):  # декоратор @property как бы формирует доступ, к тому, что мы возвращаем в качестве функции, как в переменной
        # if (dice > 0) & (dice < 7)
        return self.__hidden_num_2

    @hidden_num_2.setter
    def hidden_num_2(self, dice):
        self.__hidden_num_2 = dice



    def set_dice2(self, dice):
        self.__hidden_num_2 = dice

    def get_dice2(self):
        #if (dice > 0) & (dice < 7)
        return self.__hidden_num_2





    def throw_dices(self):
        dice_1 = random.randint(1, 6) # бросаем кости
        dice_2 = random.randint(1, 6) # бросаем кости 2
        self.current_throw+=1
        #print("Печатаю self.current_throw: ", self.current_throw)
        #print("Печатаю dice 1 и 2: ", dice_1, dice_2 )
        if self.current_throw > self.throw_num: # если количество бросков превысило запланированное

            raise Exception("Вы превысили количество попыток! ")

        if {dice_1,dice_2} == {self._hidden_num_1, self._hidden_num_2}: # Почему оформлено, как множество (только уникальные элементы?)
            return True
        else:
            return False


    def __throw_dices(self):  # просто, как пример скрытой функции
        pass




if __name__ == "__main__": # Что это???
    dice_game = Dice_incapsulation(2)
    dice_game.set_hidden_numbers()
    print(dir(dice_game)) # т.к. следующая строка ругается, мы просто можем посмотреть все , что есть методом dir
    # dice_game.__throw_dices() # так нас наругает комп, т.к. мы вызываем скрытую функцию

#    print(dice_game.__hidden_num_1, dice_game.__hidden_num_2) # я закоментил, т.к. две земли не дают пользоваться и нужно пользоваться методами get
#    print(dice_game.get_dice1(), dice_game.get_dice2())

    print(dice_game.hidden_num_1, dice_game.hidden_num_2) # подолжение истории с декоратором, обращаемся к функции,
    # как к атрибуту, при этом вызывается функйия и возвращает значение, которое она возвращает

    # dice_game.set_dice1(5) # вручную пробуем менять параметры. Попробовать работу с этим и без этого метода
    dice_game.hidden_num_1 = 5
    # dice_game.set_dice2(4)
    dice_game.hidden_num_2 = 4

    # print(dice_game.get_dice1(), dice_game.get_dice2())
    print(dice_game.hidden_num_1, dice_game.hidden_num_2)



    for i in range(4):
        try:
            print(dice_game.throw_dices())
        except:
            print("Игра закончена")