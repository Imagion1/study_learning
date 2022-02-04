

import random

num = random.randrange(1,101)

shot = int(input())
while not shot == num:
    if shot > num:
        print('Слишком много, попробуйте еще раз')
    if shot < num:
        print('Слишком мало, попробуйте еще раз')
    shot = int(input())


print('Вы угадали, поздравляем!')