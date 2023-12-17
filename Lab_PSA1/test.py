import hashlib
import random

def calculate_md5(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    return md5_hash

def generate_random_string(length=7):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(letters) for _ in range(length))

def birthday_attack():
    hash_table = {}
    found = False

    while not found:
        random_str = generate_random_string()
        md5_hash = calculate_md5(random_str)

        if md5_hash in hash_table:
            print("Collision found!")
            print(f"line 1: {hash_table[md5_hash]}")
            print(f"line 2: {random_str}")
            found = True
        else:
            hash_table[md5_hash] = random_str

birthday_attack()
