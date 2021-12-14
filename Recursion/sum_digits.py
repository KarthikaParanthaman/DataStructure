def sum_digits(num):
    if num == 0:
        return 0
    rem = num % 10
    return rem + sum_digits(num//10)

print(sum_digits(254))