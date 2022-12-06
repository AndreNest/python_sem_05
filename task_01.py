# 1) Камень - ножницы - бумага
import random
n = int(input('до раундов будем играть будем играть? '))
player_point = 0
bot_point = 0
count_nul = 0

knb = {1: 'Камень', 2: 'Ножницы', 3: 'Бумага'}
for i in range(n):
    print('--------new raund--------')
    player_choise = int(input('Сделайте выбор: 1 - камень, 2 - ножницы, 3 - бумага: '))
    bot_choise = int(random.randint(1,3))
    print(f'Вы выбрали {knb[player_choise]}, компьютер выбрал: {knb[bot_choise]}')
    if player_choise == bot_choise:
        print('Ничья')
        count_nul +=1

    elif (player_choise == 1 and bot_choise == 2) or (player_choise == 2 and bot_choise == 3) or (player_choise == 3 and bot_choise == 1):
        player_point += 1
        print(f'Вы выиграли раунд!')
    else:
        bot_point +=1
        print(f'Вы проиграли раунд!')

if player_point == bot_point:
    print(f'Вы набрали: {player_point}, соперник набрал: {bot_point}, раундов в ничью: {count_nul}')
    print('Ничья')
elif player_point > bot_point:
    print(f'Вы набрали: {player_point}, соперник набрал: {bot_point}, раундов в ничью: {count_nul}')
    print('Победа')
else:
    print(f'Вы набрали: {player_point}, соперник набрал: {bot_point}, раундов в ничью: {count_nul}')
    print('Поражение')

