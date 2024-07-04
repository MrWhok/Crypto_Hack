def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


a = int(input())
b = int(input())
print(gcd(a,b))

#The answer is 1512
