'''

map() function

'''

# Step 1
def main():
    yell("This is BOOTCAMP")


def yell(word):
    print(word.upper())


if __name__ == "__main__":
    main()


# Step 2
def main():
    yell(["This", "is", "BOOTCAMP"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()


# Step 3
def main():
    yell("This", "is", "BOOTCAMP")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()


# Step 4
def main():
    yell("This", "is", "BOOTCAMP")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()