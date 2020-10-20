''''
10.1_polymorfism
Это тоже пример полиморфизма и на уроке он на одной странице,
но я перенес на другую, т.к. при запуске на одной сторанице
запускаются спазу два и второй метод использует попытки первого и усословия первого и второго.




'''

import random
from dice_game import Dice

print()
print('    Пример полиморфизма 2 - Dice_type_2(Dice) \n' +
      'В этом примере, я опять изменил метод throw_dices(self)\n '
      'и теперь для того, что бы "Игрок-1" выйграл, нужно что бы один из его дайсов совпал с дайсом у игрока "Компьютер" \n')

class Dice_type_2(Dice):
    def throw_dices(self):
        '''
        Опять метод throw_dices(self), но здесь мы изменим и сделаем так, что
        True будет выводиться True, если хотя бы один дайс у игрока "Игрок-1" совпадал с дайсом игрока "Компьютер"
        '''
        dice_1 = random.randint(1, 6) # бросаем кости
        dice_2 = random.randint(1, 6) # бросаем кости 2
        self.current_throw+=1


        print('*Номер попытки "Игрок-1" (self.current_throw): ', self.current_throw)
        print('*Игрок "Игрок-1" (dice 1 и dice 2): ', dice_1, dice_2)

        if self.current_throw > self.throw_num: # если количество бросков превысило запланированное
            raise Exception("*Вы превысили количество попыток! ")

        if (dice_1 in {self._hidden_num_1, self._hidden_num_2}) or (dice_2 in {self._hidden_num_1, self._hidden_num_2}):
            ''' 
            Новое условие, когда совпало хотя бы одно значение
            '''
            return True
        else:
            return False

if __name__ == '__main__':
        # game = Dice(1)
    game_type_2 = Dice_type_2(20)  # Не понимаю, что я меня числом в скобках
    game_type_2.set_hidden_numbers()
    print('*Игрок "Компьютер" (_hidden_num_1 и_hidden_num_2) : ', game_type_2._hidden_num_1,game_type_2._hidden_num_2)
    for i in range(3):
        '''
        число в скобках = количество бросков, которое сделает 'Игрок-1', 
        что бы угадать комбинацию игрока "Компьютер"  
        '''
        try:
            print(game_type_2.throw_dices())
        except:
            print("Игра закончена")

