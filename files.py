import random
name1 = input("Hey, please write your name: ")
name2 = input("Hello, how do you wanna call?: ")

def main():
    player1 = 0
    player2 = 0
    rounds = 1

    while rounds <= 3:
        print("Round " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("{}: ".format(name1) + str(player1))
        print("{}: ".format(name2) + str(player2))
       

        rounds +=1
        
        if player1 == player2:
            print("Draw!")
        elif player1>player2:
            print("{} wins, congrats!".format(name1))
        else:
            print("{} wins, congrats!".format(name2)) 
        print("---------------------")               

       
def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main() 






    