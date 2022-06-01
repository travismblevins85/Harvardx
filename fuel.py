"""Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 
1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, less than 1% remains, output 
E instead to indicate that the tank is empty. And if more than 99% remains, output F instead to indicate that the tank is full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) 
Be sure to catch any exceptions like ValueError or ZeroDivisionError."""

import fractions

# Need to make fraction X/Y format

while True:
    gauge = input("Fraction: ")
    try:
        f1, f2 = gauge.split("/")
        # Convert from string
        int1 = int(f1)
        int2 = int(f2)
        # Make fraction
        frac = fractions.Fraction(int1/int2)
        
        # Need to keep asking for input, or break loop if input correct
        if frac <= 1:
            break
    except ValueError: 
        pass
    except ZeroDivisionError:
        pass
        # Display percentages 
perc = int(frac * 100)


if perc >= 99:
    print("F")
elif perc <= 1:
    print("E")
else:
    print(f"{perc}%")      

