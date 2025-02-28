#1
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_nums = even_numbers(n)

print(", ".join(str(num) for num in even_nums))

#2
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
divisible_nums = divisible_by_3_and_4(n)

for num in divisible_nums:
    print(num, end=" ")

#3
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))
square_nums = squares(a, b)

for square in square_nums:
    print(square, end=" ")

#4
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))
countdown_nums = countdown(n)

for num in countdown_nums:
    print(num, end=" ")
