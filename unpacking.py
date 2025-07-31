'''

Unpacking (*args, **kwargs)

'''

# Step 1
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print(total(100, 50, 25), "Knuts")


# Step 2: Modification with a list
coins = [100, 50, 25]
print(total(coins[0], coins[1], coins[2]), "Knuts")


#  Step 3: Modification with *args
coins = [100, 50, 25]
print(total(*coins), "Knuts")


# Step 4: Convert the list to a dictionary
print(total(galleons=100, sickles=50, knuts=25), "Knuts")

coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")


# Step 5: Modification with **kwargs
print(total(**coins), "Knuts")


# Step 6: Modification with *args and **kwargs
def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)


def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)
