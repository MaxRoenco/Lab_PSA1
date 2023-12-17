from random import randint

dep = 1000

while dep > 0:
    stop = int(input("Withdrawal of money - 0\nContinue - 1\n"))
    if stop == 0:
        break
    print("Your depozit: ", dep, "$")
    bet = int(input("Input your bet: "))
    predict = int(input("Choose\nred - 0\nblack - 1: \n"))
    rand = int(randint(0, 1))
    if rand == predict:
        dep += bet
        print("You are win!)")
    else:
        dep -= bet
        print("You are lose!(")

print("You won:", dep, "$")