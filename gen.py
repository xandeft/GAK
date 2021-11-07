import string
import random

def gen():
    dic = ""
    ll = ["a-z", "A-Z", "0-9", "@-#"]
    
    for i in range(5):
        choice = random.choice(ll)
        if (choice == "a-z"):
            dic += string.ascii_lowercase
        elif (choice == "A-Z"):
            dic += string.ascii_uppercase
        elif (choice == "0-9"):
            dic += string.digits
        elif (choice == "@-#"):
            dic += string.punctuation
    
    return dic

def main():
    print(gen())

if __name__ == "__main__":
    main()
