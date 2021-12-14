
def odd_even(n):
    if n & 1 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

num = input("enter num: \n")
num = int(num)
odd_even(num)