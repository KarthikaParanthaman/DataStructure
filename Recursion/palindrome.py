def palindrome(num, n):
    if n == 0:
        return 0
    r = n%10
    rev = r  + palindrome(num,n//10) * 10
    if num == rev:
        return True
    else: 
        return False

print(palindrome(544,544))
    