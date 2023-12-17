from random import randint

while True:
    n = int(input("Number of simulations: "))
    total_tosses = []
    for i in range(n):
        result = 0
        tosses = 0
        while result != 1:
            result = randint(0, 1)
            tosses += 1
        total_tosses.append(tosses)

    avg = sum(total_tosses)/n
    print(2**avg)