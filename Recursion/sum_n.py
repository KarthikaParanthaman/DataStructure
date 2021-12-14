def sum_n(n):
    if n == 0:
        return n 
    sum = n + sum_n(n-1)
    return sum

print(sum_n(5))