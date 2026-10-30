def ispoweroftwo(n):
    if n <= 0:
        return False

    while n % 2 == 0:
        n = n // 2

    return n == 1

num = int(input("enter a number: "))

print(ispoweroftwo(num))
