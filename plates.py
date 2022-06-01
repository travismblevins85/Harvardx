"""In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements 
or Invalid if it does not. Assume that any letters in the usr’s input will be uppercase. Structure your program per the below, 
wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to 
implement additional functions for is_valid to call (e.g., one function per requirement)."""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    # Has to begin with letters  and end with numbers
    # cannot have numbers in the middle
    # First number used cannot be a 0
    for c in s:
        if c in ["!",".","?",' ']:
            return False
    x = s[len(s)//2]
    if s[:2].isnumeric() or x == '0':
        return False
    elif len(s)-1 > 6 or len(s)-1 < 2:
        return False
    elif x.isnumeric() and s[-1].isalpha():
        return False
    else:
        return True

main()   


