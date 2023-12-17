from random import randint

n = int(input("Input number of executes: "))
slot = int(input("Input number of barrel slots: "))
bullets = int(input("Input number of bullets in barrel "))
adjacent = int(input("1 - adjacent slots\n2 - not adjacent slots\n"))
roll = int(input("1 - roll after the first pull of the trigger\n2 - without roll\n"))
revolver = []
dead = 0
for _ in range(n):

    revolver = [0] * slot

    if adjacent == 1:
        for _ in range(bullets):
            j = randint(0, slot - 1)
            i = (j + 1) % slot
            revolver[i] = 1
            revolver[j] = 1

    elif adjacent == 2:
        for _ in range(bullets):
            j = randint(0, slot - 1)
            i = randint(0, slot - 1)
            while i == j or i == (j + 1) % slot or i == (j - 1) % slot:
                i = randint(0, slot - 1)
            revolver[i] = 1
            revolver[j] = 1

    chosen_b = randint(0, slot - 1)
    while revolver[chosen_b] == 1:
        chosen_b = randint(0, slot - 1)

    if roll == 1:
        chosen_b = randint(0, slot - 1)
    elif roll == 2:
        chosen_b += 1

    if revolver[chosen_b % slot] == 1:
        dead += 1

print("Probabilitate to be alive: ", 1 - dead/n)









