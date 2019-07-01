"""
roll dice for three times. Big or small
"""

import random

def dice(numbers = 3, points = None):
    print('<<<<< ROLE THE DICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers = numbers - 1
    return points

def result(total):
    if 11 <= total <= 18:
        return 'Big'
    elif 3 <= total <= 10:
        return 'Small'

def start_game():
    print('<<<<< GAME STARTS! >>>>>')
    choices = ['Big', 'Small']
    your_choice = input('Big or Small: ')
    if your_choice in choices:
        points = dice()
        total = sum(points)
        YouWin = your_choice == result(total)
        if YouWin:
            print('The points are', points, 'You win!')
        else:
            print('The points are', points, 'You lose!')
    else:
        print('Invalid Words')
    return

start_game()

"""
Solution 2:

import random

while True:
    print('<<<<< GAME STARTS! >>>>>')
    choice = input('Big or Small: ')
    print('<<<<< ROLE THE DICE! >>>>>')
    
    point1 = random.randrange(1, 7)
    point2 = random.randrange(1, 7)
    point3 = random.randrange(1, 7)
    
    dice_list = [point1, point2, point3]
    total = sum(dice_list)
    
    def dice(total):
        if total in range(11, 19):
            return 'Big'
        else:
            return 'Small'
    
    lst = dice(total)
    
    if lst == choice:
        print('The points are', dice_list, 'You win!')
    else:
        print('The points are', dice_list, 'You lose!')
"""
