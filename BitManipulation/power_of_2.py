def power_of_2(num):
    if num & num-1 == 0:
        return True
    return False

print(power_of_2(5))
print(power_of_2(8)