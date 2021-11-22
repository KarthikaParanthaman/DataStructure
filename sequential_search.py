def sequential_search(data, elt):
    for i in range(len(data)):
        if data[i] == elt :
            return i
    return None

data = [1,5,8,2,9,10,4,3]
elt = 8 # find this number
elt = 11
print(sequential_search(data,elt))
