from random import randint

n = int(input("Number of simulations: "))

sum_of_money = 0

for _ in range(n):
    money = 0
    lst = [1, 2, 3, 4]
    bet = 0

    while len(lst):
        if len(lst) > 1:
            bet = lst[0] + lst[-1]
        elif len(lst) == 1:
            bet = lst[0]

        won = bool(randint(0, 1))
        if won:
            del lst[0]
            if len(lst) > 1:
                del lst[-1]
            money += bet
        else:
            lst.append(bet)
            money -= bet
    sum_of_money += money

print("Avg profit: ", sum_of_money/n, "$")