import random
import replit

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# 카드 추가 함수
def append_and_score(cards_list):
    """카드를 추가하고 카드들의 합을 반환"""
    new_card = random.choice(cards)
    cards_list.append(new_card)
    return sum(cards_list)

def judge():
    if your_score > 21:
        print("You went over. You lose.")
    elif com_score > 21:
        print("Computer went over. You win!")
    elif your_score > com_score:
        print("You win!")
    elif your_score < com_score:
        print("You lose.")
    elif your_score == com_score:
        print("Draw")

# 카드 리스트
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# 게임 시작
re_game = True
while re_game:
    print(logo)
    # 2개의 카드 첫 분배
    your_cards = []
    com_cards = []
    for i in range(2):
        your_score = append_and_score(your_cards)
        com_score = append_and_score(com_cards)
    
    # 플레이어가 카드를 더 뽑을지 결정  
    re_pick = True
    while re_pick:
        print(f"    Your cards: {your_cards}, current score: {your_score}")
        print(f"    Computer's first card: {com_cards[0]}")
        pick_another = input("Type 'y' to get another card, type 'n' to pass: ")
        if (not pick_another == 'y'):
            re_pick = False
        else:
            your_score = append_and_score(your_cards)
            if your_score > 21:
                re_pick = False

    # 컴퓨터(딜러)의 카드합이 16 이하이면 새로운 카드를 한장 더 뽑음
    # 2번째 카드 이후의 11은 합이 21이 넘으면 1로 계산
    while com_score <= 16:
        com_score = append_and_score(com_cards)
        if com_cards[-1] == 11 and com_score > 21:
            com_cards[-1] = 1
    
    print(f"    Your final hand: {your_cards}, final score: {your_score}")
    print(f"    Computer's final hand: {com_cards}, final_score: {com_score}")
    judge()
    re_game_yn = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if re_game_yn == 'n':
        re_game = False
    replit.clear()