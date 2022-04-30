# python name.py Travis
# Output: Hello, my name is Travis

import sys

try:
    print("Hello, my name is ", sys.argv[1])
except IndexError:
    print("Too few arguments")    

    # or work around exceptions

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])            
