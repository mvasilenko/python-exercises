
def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3*number + 1
    print(number)
    return number


def input_number(i=None):
    while i is None:
        print("Enter number:")
        try:
            i = int(input())
        except ValueError:
            print("Please enter integer!")
    return i


def main():
    i = input_number()
    while i != 1:
        i = collatz(i)


if __name__ == "__main__":
    main()
