def get_bit(num, pos):
    # 1010 - pos 1, result =1
    mask = 1 << pos
    result = num & mask
    return result

def clear_bit(num, pos):
    # 1010 pos 1 , 1000
    mask = ~(1 << pos) #~(0010) 1101
    result = num & mask
    return result


num = 1010
pos = 1
print(get_bit(num, pos))
print(clear_bit(num, pos))