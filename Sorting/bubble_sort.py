def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swap = 0
        j = 0
        while j < n-1:
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1] , data[j]
                print(i, j, j+1)
                swap = 1
            j += 1
        if swap == 0 :
            break


data =[1,5,7,8,2]
bubble_sort(data)
print(data)