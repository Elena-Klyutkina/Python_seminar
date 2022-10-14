# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ''интеллектом''

import random
from random import randint

def input_dat(name):
    x = int(input(f'{name}, введите количество конфет, которое возьмете от 1 до 28: '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, введите корректное количество конфет: '))
    return x

def p_print(name, k, counter, value):
    print(f'Ходил(а) {name}, он(а) взял(а) {k}, теперь у него(нее) {counter} конфет. Осталось на столе {value} конфет.')

def bot_input(count, user_input):
    key_number = 29
    if (count - (key_number - user_input)) % key_number == 0:
        step = key_number - user_input
    else:
        step = count % key_number
    if step == 0:
        step = 1
    if step > count:
        step = count
    print(f'БОТ забрал {step} конфет')
    return step

player1 = input('Введите имя первого игрока: ')
flag_bot = 'false'
if input('Вы хотите сыграть с ботом? Если "да", то введите "да". Если нет, то введите любое значение. \n').upper() == 'ДА':
    player2 = 'БОТ'
    flag_bot = 'true'
else:
    player2 = input('Введите имя второго игрока: ')
value = int(input('Введите количество конфет на столе: '))

# Жребьевка:
players = [player1, player2]
while len(players) == 2: 
    player = random.choice(players)
    print(f'Игроку {player} выпал первый ход')
    players.remove(player)
    
flag = randint(0, 2) # флаг очередности

counter1 = 0 
counter2 = 0

if flag_bot == 'false':
    while value > 28:
        if flag:
            k = input_dat(player1)
            counter1 += k
            value -= k
            flag = False
            p_print(player1, k, counter1, value)
        else:
            k = input_dat(player2)
            counter2 += k
            value -= k
            flag = True
            p_print(player2, k, counter2, value)

    if flag:
        print(f'Выиграл {player1}')
    else:
        print(f'Выиграл {player2}')
        
else:
    while value > 28:
        if flag:
            k = input_dat(player1)
            counter1 += k
            value -= k
            flag = False
            p_print(player1, k, counter1, value)
        else:
            k = bot_input(value, k)
            counter2 += k
            value -= k
            flag = True
            p_print(player2, k, counter2, value)

    if flag:
        print(f'Выиграл {player1}')
    else:
        print(f'Выиграл {player2}')