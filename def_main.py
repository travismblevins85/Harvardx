def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))# In the beginning it doesn't know square(x) yet, not defined yet

def square(n):
    return n**2

main()        