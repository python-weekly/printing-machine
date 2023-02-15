# The entry point of you application
from assets import art
from src.printer import Printer


def main():
    print(art.logo)
    printer = Printer()
    printer.start()


if __name__ == '__main__':
    main()
