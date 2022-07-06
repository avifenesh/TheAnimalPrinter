from validators import url
from animal_printer import printer
import argparse


def main():
    parser = argparse.ArgumentParser(description="url to wiki page with animal table")
    parser.add_argument("url", type=str)
    args = parser.parse_args()
    if not url(args.url):
        raise Exception("This not a valid URL, please try again with valid one")
    else:
        return printer(args.url)


if __name__ == "__main__":
    main()
