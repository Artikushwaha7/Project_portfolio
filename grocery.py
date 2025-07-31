'''
Dict Data Structure
Variables
Loops
Conditionals
Input/Output
Error Handling : https://docs.python.org/3/tutorial/errors.html

'''


from collections import defaultdict

grocery_list = defaultdict(int)

while True:
    try:
        item = input().strip().upper()

        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:

        for item in sorted(grocery_list):
            print(grocery_list[item], item)

        break