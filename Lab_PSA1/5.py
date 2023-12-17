import hashlib

myHash = input("Enter hashed password: ")
hash_object = hashlib.md5(myHash.encode())
print(hash_object.hexdigest())

#3fc0a7acf087f549ac2b266baf94b8b1

input_hashed = hash_object.hexdigest()

password_file = open('passwords.txt', 'r')

try:
    for word in password_file:
        encoding_word = word.encode('utf-8')
        hashed_word = hashlib.md5(encoding_word.strip())
        digesting = hashed_word.hexdigest()

        if digesting == input_hashed:
            print("Password is: ", word)
            password_file.close()
            break
except:
    print("Password not found")
