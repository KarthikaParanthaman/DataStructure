def last_index(data,n,key):
    if n == -1 :
        return -1
    if data[n] == key:
        return n
    return last_index(data,n-1,key)

def last_index1(data,i,n,key):

    if  i == n :
        return -1
    index = last_index1(data, i+1, n, key)        
    if index == -1:
        if data[i] == key:
            return 0
        else:
            return -1
    else:
        return index+1


    

data = [1,2,3,4,11,1,5]
print(last_index(data,len(data)-1,1))
print(last_index1(data,0, len(data)-1, 1))