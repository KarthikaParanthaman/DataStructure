def find_index(data, i, n,key):
    if i == n:
        return -1
    if data[i] == key:
        return i
    return find_index(data, i+1,n ,key)
    

print(find_index(range(10),0, 10, 4))


