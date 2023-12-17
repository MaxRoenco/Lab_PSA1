from random import randint

n = int(input("Input number of executions: "))
dep_1 = int(input("Input dep: "))
win = dep_1 * 2
lst = [dep_1/10] * 10
lose = 0
victory = 0
sum_money = 0
for _ in range(n):
    dep = dep_1
    lst = [dep_1 / 10] * 10
    while win > dep > 0:
        if len(lst) == 0:
            break
        result = randint(0, 1)
        if result == 0 and len(lst) != 1:
            dep = dep + lst[0] + lst[-1]
            lst.pop(0)
            lst.pop(-1)
        elif result == 0 and len(lst) == 1:
            dep = dep + lst[0]
            lst.pop(0)
            break
        elif result == 1:
            dep = dep - lst[0] - lst[-1]
            lst.append(lst[0] + lst[-1])
        if len(lst) == 0:
            break
    if dep <= 0:
        lose += 1
    else:
        victory += 1
    sum_money += dep
    print(dep)
print("Lose: ", lose)
print("Win: ", victory)
print(sum_money, "$")
