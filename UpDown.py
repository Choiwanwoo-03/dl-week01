# 선문대학교 컴퓨터공학부
# 2022243101 최완우
# 업 다운 숫자 맞추기

import random

random_number = random.randint(1, 100)

game_count = 1
while True :
    if (game_count > random_number) :
        print("{game_count} 보다 작습니다.")
    elif (game_count < random_number) :
        print("{game_count} 보다 큽니다.")
    else :
        print("정답입니다.")