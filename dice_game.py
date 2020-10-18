# скопировал сюда игру в кости из прошлого урока, для новой темы 10.1_polymorfism

import random
class Dice:
    def __init__(self, N):
        ''''
        N это Количество бросков, которое сделает "Игрок-1",
        что бы угадать комбинацию игрока "Компьютер"
        '''
        self.throw_num = N
        self.current_throw = 0 # Параметр отвечает за количество совершенных бросков

    def set_hidden_numbers(self):  # Это сколько выпало у компьютерра?
        '''
        Это виртуальный игрок, он загадывет какие то кости,
        точнее выбирает их рандомно.
        Назову его игрок "Компьютер"
        '''
        self._hidden_num_1 = random.randint(1,6)  # _'земля' в начале, значит, что параметры скрытые
        self._hidden_num_2 = random.randint(1,6)
        # print("печатаю self._hidden_num 1 и 2: ", self._hidden_num_1, self._hidden_num_2)         # это я мониторю

    def throw_dices(self):
        '''
        Это второй игрок назову его "Игрок-1"
        он пытается угадать (делает N количество попыток)
        комбинацию выпавшую и игрока "Компьютер"
        '''
        dice_1 = random.randint(1, 6) # бросаем кости
        dice_2 = random.randint(1, 6) # бросаем кости 2
        self.current_throw+=1
        ''''
        Счетчик количества бросков "Игрок-1"
        '''
        print('Номер попытки "Игрок-1" (self.current_throw): ', self.current_throw)
        print('Игрок "Игрок-1" (dice 1 и dice 2): ', dice_1, dice_2 )
        if self.current_throw > self.throw_num: # если количество бросков превысило запланированное

            raise Exception("Вы превысили количество попыток! ")

        if {dice_1,dice_2} == {self._hidden_num_1, self._hidden_num_2}:
            ''''
            Здесь описано условие, как будут сравниваться выпавшие на дайсах результаты
            True = комбинации совпали
            '''
            return True
        else:
            return False

if __name__ == "__main__": # Что это???
    dice_game = Dice(10)
    dice_game.set_hidden_numbers()
    print('Игрок "Компьютер" (_hidden_num_1 и_hidden_num_2) : ', dice_game._hidden_num_1, dice_game._hidden_num_2)

    for i in range(2):
        '''
        Здесь мы указываем, сколько можно сделать попыток игроку "Игрок-1".
        И если это количество будет больше разрешенного, 
        то будет выводиться сообщение "Игра закончена" 
        ТОлько почему то перестало работать
        '''
        try:
            print(dice_game.throw_dices())
        except:
            print("Игра закончена")