"""Suppose that you’re in the habit of making a list 

of items you need from the grocery store.

In a file called grocery.py, implement a program 
that prompts the user for items, one per line, until 
the user inputs control-d (which is a common way of 
ending one’s input to a program). Then output the 
user’s grocery list in all uppercase, sorted 
alphabetically by item, prefixing each line with the 
number of times the user inputted that item. No need 
to pluralize the items. Treat the user’s input 
case-insensitively."""


# Grocery dict

groceries = {}
# Make a forever loop with while 
while True:
    try:

# Prompt user for items
        x = input().lower()

        if x in groceries:
            groceries[x] += 1
        # If user just wants one
        else:
            groceries[x] = 1    
# Output user's grocery list alphabetically and with amount before, upper()
    except EOFError:
        # When user ends program
        for key in sorted(groceries.keys()):
            print(groceries[key], key.upper())
            # Stop the loop
        break