import random
from random import randint
from random import randint, shuffle

coin = random.choice(["heads", "tails"]) # 50% chane, depending on how many parameter you enter
print(coin)

number = randint(1, 10)
print(number)

cards = ['jack', 'queen', 'king']
shuffle(cards)
for card in cards:
    print(card)

