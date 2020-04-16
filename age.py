import datetime

user_name = input("Hey, what should i call you? ")

while True:
    birth_year = input("What year were you born? ")
    try:
        birth_year = int(birth_year)
    except ValueError:
        continue
    else:
        break  

current_year = 2020
current_age = current_year - birth_year

turn_25 = (25-current_age) + current_year
turn_50 = (50-current_age) + current_year
turn_75 = (75-current_age) + current_year
turn_100 = (100-current_age) + current_year

if turn_25 > current_year:
    print("You will turn 25 in {}, {}".format(turn_25, user_name))
if turn_50 > current_year:
    print("You will turn 50 in {}, {}".format(turn_50, user_name))
if turn_75 > current_year:
    print("You will turn 75 in {}, {}".format(turn_75, user_name))
if turn_100 > current_year:
    print("You will turn 100 in {}, {}".format(turn_100, user_name))

