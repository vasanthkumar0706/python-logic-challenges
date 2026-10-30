
def count_days(a, b, c, d):
    start = max(a, c)
    end = min(b, d)

    if start > end:
        return 0
    else:
        return end - start + 1

a = int(input("Alice arrival day: "))
b = int(input("Alice leaving day: "))

c = int(input("Bob arrival day: "))
d = int(input("Bob leaving day: "))

print("Days Together:", count_days(a, b, c, d))
