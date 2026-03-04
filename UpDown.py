# 선문대학교 컴퓨터공학부
# 2022243101 최완우
# 업 다운 숫자 맞추기

import random

random_number = random.randint(1, 100)

game_count = 1
while True :
    try :
        my_number = int(input("1 ~ 100 사이의 숫자를 입력하세요"))
        if my_number > random_number :
            print("Down")
        elif my_number < random_number :
            print("Up")
        elif my_number == random_number :
            print("Collect")
            
        game_count += 1
    except :
        print("Except")