
def comma_code(spam):
    spam[-1] = "and " + spam[-1]
    return ", ".join(spam)


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    spam = []
    if len(spam) == 0:
        return
    print(comma_code(spam))


if __name__ == "__main__":
    main()
