from art import logo, vs
from game_data import data
import random
from replit import clear

def compare(A,B):
    """팔로워 수를 비교"""
    if A['follower_count'] >= B['follower_count']:
        return 'a'
    elif A['follower_count'] < B['follower_count']:
        return 'b'

def print_info(id):
    """계정의 정보 출력"""
    return f"{id['name']}, a {id['description']}, from {id['country']}."

def user_choice_fnt():
    """A와 B 중 사용자의 선택을 반환"""
    while 1:
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == 'a' or user_choice == 'b':
            return user_choice
        else:
            print('Wrong input. Try again.')

            
def game():
    # 사용자의 점수
    score = 0
    # 처음 비교할 계정 선택
    celeb_a = random.choice(data)
    celeb_b = random.choice(data)
    while celeb_a == celeb_b:
        celeb_b = random.choice(data)
    
    continue_game = True
    while continue_game:
        print(logo)
        # 점수 출력
        if score != 0:
            print(f"You're right. Current score: {score}")
            
        # 비교할 계정 출력
        print("Compare A: " + print_info(celeb_a))
        print(vs)
        print("Against B: " + print_info(celeb_b))
        
        # 사용자의 선택을 받음
        user_choice = user_choice_fnt()
        
        clear()
        if user_choice == compare(celeb_a, celeb_b):
            # 사용자의 선택이 맞으면 점수 추가 후 A를 B의 값으로 바꾸고 B는 새로 뽑음 
            score += 1
            celeb_a = celeb_b
            celeb_b = data.pop(random.randint(0,len(data)-1))
        else:
            # 사용자의 선택이 틀리면 점수 출력 후 게임 종료
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False


game()





