from random import randint

n = int(input("Input number of executions: "))
dep = int(input("Input deposit: "))
bet = int(input("Input your first bet: "))
win = dep * 2
lose = 0
victory = 0
sum_lose = 0
sum_victory = 0

for _ in range(n):
    current_dep = dep
    current_bet = bet

    while current_dep > 0 and current_dep < win:
        result = randint(0, 1)
        if result == 0:
            current_dep += current_bet
            current_bet = bet
        elif result == 1:
            current_dep -= current_bet
            current_bet *= 2
    if current_dep <= 0:
        lose += 1
        sum_lose += current_dep
    else:
        victory += 1
        sum_victory += current_dep
    print(current_dep)
print("Lose: ", lose)
print("Sum of lose: ", sum_lose, "$")
print("Win: ", victory, )
print("Sum of Win: ", sum_victory, "$")
print("General sum: ", sum_victory + sum_lose, "$")