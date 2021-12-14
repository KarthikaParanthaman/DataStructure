def single_occurence(data):
    result = 0
    for i in data:
        result ^= i
    return result

data = [1, 2, 3, 1, 2, 3, 4]
result = single_occurence(data)
print(result)