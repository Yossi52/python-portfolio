#Number Guessing Game Objectives:
logo = """
 __    _  __   __  __   __  _______  _______  ______      _______  __   __  _______  _______  _______ 
|  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |    |       ||  | |  ||       ||       ||       |
|   |_| ||  | |  ||       || |_|   ||    ___||   | ||    |    ___||  | |  ||    ___||  _____||  _____|
|       ||  |_|  ||       ||       ||   |___ |   |_||_   |   | __ |  |_|  ||   |___ | |_____ | |_____ 
|  _    ||       ||       ||  _   | |    ___||    __  |  |   ||  ||       ||    ___||_____  ||_____  |
| | |   ||       || ||_|| || |_|   ||   |___ |   |  | |  |   |_| ||       ||   |___  _____| | _____| |
|_|  |__||_______||_|   |_||_______||_______||___|  |_|  |_______||_______||_______||_______||_______|
"""

import random


def lives_calc(lives):
    """목숨의 수 계산과 목숨 수에 따른 상태 출력"""
    lives -= 1
    if lives == 0:
        print("You've run out of guess, you lose.")
    else:
        print("Guess agian.")
    return lives

def choose_lives():
    """난이도 선택에 따른 목숨의 수 반환"""
    while 1:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5
        else:
            print("Wrong input.")


# 로고, 인사 출력
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# 랜덤 숫자 선택
com_guess = random.randint(1,100)

# 난이도 선택에 따른 목숨 수
remain_lives = choose_lives()

# 목숨이 남아 있을 때 까지 게임 실행
while remain_lives > 0:
    print(f"You have {remain_lives} attemts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess > com_guess:
        print("Too high.")
        remain_lives = lives_calc(remain_lives)
    elif user_guess < com_guess:
        print("Too low.")
        remain_lives = lives_calc(remain_lives)
    elif user_guess == com_guess:
        print(f"You got it! The answer was {com_guess}")
        break