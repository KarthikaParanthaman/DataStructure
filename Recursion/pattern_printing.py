def print_pattern(n):
    if n == 0:
        return
    print_pattern(n-1)
    for i in range(1, n+1):
        print(i, end =" ")
    print()
  

def print_pattern_rev(n):
    if n == 0:
        return
    for i in range(1, n+1):
        print(i, end =" ")
    print()
    print_pattern_rev(n-1)
    
def print_pattern_all(n):
    if n == 1:
        print(n)
        return 1
    for i in range(1, n+1):
        print(i, end =" ")
    print()
    print_pattern_all(n-1) 

    for i in range(1, n+1):
        print(i, end =" ")
    print()          
    
print_pattern_all(5)