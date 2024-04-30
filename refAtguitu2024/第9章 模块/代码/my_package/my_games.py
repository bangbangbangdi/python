import random

def game1():  # 石头剪刀布
    player_score,computer_score = 0,0
    for i in range(3):
        player = input('请输入石头剪刀布：')
        computer = random.choice(['石头','剪刀','布'])
        print('电脑出的是',computer)
        if player ==computer:
            player_score+=1
            computer_score+=1
        elif (player=='石头' and computer=='剪刀') or (player == '剪刀' and computer == '布') or (player=='布' and computer=='石头'):
             player_score+=1
        else:
            computer_score+=1
        print('玩家得分%d 电脑得分%d'%(player_score,computer_score))
    if player_score==computer_score:
        print('平局')
    elif player_score>computer_score:
        print('玩家胜利')
    else:
        print('电脑胜利')

def guess_number(start,end):
    number = random.randint(start,end)
    while True:
        player = int(input('请输入你猜的数字：'))
        if player == number:
            print('猜中了！')
            break
        elif player>number:
            print('猜大了')
        else:
            print('猜小了')