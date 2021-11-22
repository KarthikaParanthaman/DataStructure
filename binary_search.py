def binary_search(data, elt):
    low = 0
    high = len(data)

    while low < high:
        mid = (low+high) // 2
        if elt < data[mid]:
            high = mid -1
        elif elt == data[mid]:
            return mid
        elif elt > data[mid]:
            low = mid+1
    
    return None

def rbinary_search(data,elt,low, high):
    mid = (low+high) // 2

    if low > high:
        return False
    else:
        if elt < data[mid]:
            return rbinary_search(data,elt,low, mid -1)
        elif elt > data[mid]:
            return rbinary_search(data,elt, mid+1,high)
        elif elt == data[mid]:
            return mid


data =[1,3,4,5,6,7,8,9,11,12]
elt = 81
print(rbinary_search(data, elt,0,len(data)-1))