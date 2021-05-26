def super_digit(n):
    if(n<10):
        return n
    else:
        sum = n%10 + super_digit(n//10)
    if sum>9:
        sum = super_digit(sum)
    return sum

print(super_digit(9758))

