#1
def convert (grams):
    ounces = grams / 28.3495231
    print(f"{grams} grams in ounces : {ounces:.4f}")
grams = int(input("enter grams: "))
convert (grams)

#2
def convert ():
    farenheit = int (input("input temperature in Farenheit: "))
    celsium = (5 / 9) * (farenheit - 32)
    print(f"temperature in Celsium is: {celsium:.1f}")
convert()  

#3
numheads = int(input("enter number of heads: "))
numlegs = int(input("enter number of legs: "))

def solve(numheads, numlegs):
    rabbits = numlegs / 2 - numheads
    chickens = numheads - rabbits
    print (f"number of rabbits: {int(rabbits)}") 
    print (f"number of chickens: {int(chickens)}")

solve(numheads, numlegs)

#4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(nums):
    return [num for num in nums if is_prime(num)]

nums = list(map(int, input("Enter a list of numbers: ").split()))
primes = filter_prime(nums)
print(f"Prime numbers: {primes}")

#5
from itertools import permutations

def string_permutations():
    user_input = input("Enter a string:")
    perm = permutations(user_input)
    for p in perm:
        print(''.join(p))

#6
def reverse_sentence():
    user_input = input("Enter a sentence:")
    word = user_input.split()
    sentence = ' '.join(reversed(word))
    print(sentence)

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8
def spy_game(n):
    for i in range(len(n) - 2):
        if n[i:i+3] == [0, 0, 7]:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#9
def volume():
    radius = int(input("enter the radius of sphere: "))
    pi = 3.14
    volume = 4/3 * pi * pow(radius, 3)
    print(f"volume of the sphere is: {volume:.2f}")
volume()

#10
def unique_elements(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

numbers = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8]
result = unique_elements(numbers)
print(result)

#11
def ispalindrome(word):
    if word == word[::-1]:
        return True
    return False

word = input("enter the word: ")
print(ispalindrome(word))

#12
def histogram(nums):
    for num in nums:
        print ('*' * num)
        
histogram([4, 9, 7])

#13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
guess_the_number()