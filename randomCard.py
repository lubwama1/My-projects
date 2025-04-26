
import random

def randomCard():
    cards = ['¥', '$', '€']
    
    while True:
        current_card = random.choice(cards)
        user_input = input('Guess the current currency (€, $, ¥) or q to quit:\n ')
        
        if user_input.lower() == 'q':
            break
        elif user_input == current_card:
            print(f'{user_input} is correct ✅')
        else:
            print(f'Sorry, {user_input} is wrong. The correct answer was {current_card}')
            
if __name__ == '__main__':
    randomCard()