import argparse
import random
from gen import gen 

def run(args):
    password = ""
    dic = gen()
    for i in range(args.amount):
        password += random.choice(dic)
    
    print("Password: {}".format(password))

def main():
    parser = argparse.ArgumentParser(description="Generate strong password")
    parser.add_argument("-n", help="number of caracteres on the password", dest="amount", type=int, required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
