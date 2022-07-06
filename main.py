from validators import url
from sys import argv
from animalPrinter import printer

def main():
    print(argv[1])
    if not url(argv[1]):
        raise Exception("This not a valid URL, please try again with valid one")
    else:
        printer(argv[1])

if __name__ == "__main__":
    main()