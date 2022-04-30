"""Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, \
    10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, 
each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the 
user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

# Amount owed 
due = 50

while due > 0:
    print("Amount Due: ", due)
    # Insert a coin
    insert = int(input("Insert Coin: ")) 
    # Can only be 25, 10, or 5

    if insert in [5, 10, 25]:
        due -= insert

# Show amount owed
owed =  abs(due)

# Print it

print("Change owed: ", owed)

