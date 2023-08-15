a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print(f"maximum is {maximum}")
