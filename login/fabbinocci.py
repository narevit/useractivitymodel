def fabonacci(n):
    if n < 0:
        print("Not allowed")
    elif n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fabonacci(n-1)+fabonacci(n-2)

print(fabonacci(3))