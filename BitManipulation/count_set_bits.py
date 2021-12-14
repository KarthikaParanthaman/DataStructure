def count_bits_set(num):
    count = 0
    while num > 0:
        num =num & num-1
        count +=1
    return count

print(count_bits_set(13))

# 13 1101
# 1101 & 1100 = 1100 - 1
# 1100 & 1011 - 1000 - 2
# 1000 & 0111 - 0111 - 3