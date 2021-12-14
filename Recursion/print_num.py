def print_asc(n):
    if n == 0 :
        return
    print_asc(n-1)
    print(n)
    
def print_desc(n):
    if n == 0 :
        return
    print(n)
    print_desc(n-1)

print("ascending")
print_asc(10)
print("descending")
print_desc(10)