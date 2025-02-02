#1
def convert(grams):
    return  28.3495231 * grams
    
print(convert(5))

#2
def temperature(F):
    return (5 / 9) * (F-34)

print(temperature(10))

#3
def solve(numheads,numlegs):
   r = (numlegs - 2 * numheads) // 2
   c = numheads - r
   return c, r

print(solve(35,94))

#4
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if prime(num)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filter_prime(numbers))

#5
import itertools
def permutations():
    user_input = input()
    
    permutation = itertools.permutations(user_input)
    
    for x in permutation:
        print(''.join(x))

permutations()

#6
def word_reverse(string):
    word = string.split()
    reverse = word[::-1]
    sentence = ' '.join(reverse)
    return sentence

string = input()
print(word_reverse(string))

#7
def has_33(num):
    for i in range(len(num) - 1):
        if num[i] == 3 and num[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))

#8
def spy_game(nums):
    find = [0, 0, 7]
    ind = 0
    
    for num in nums:
        if num == find[ind]:
            ind += 1  
        if ind == len(find):  
            return True
    return False

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0]))

#9
import math
def volume(radius):
    return 4/3 * math.pi * radius**3

print(volume(10))

#10
def unique(nums):
    uniq_list = []
    for num in nums:
        if num not in uniq_list:
            uniq_list.append(num)
    return uniq_list

print(unique([1, 2, 3, 1, 4, 5, 5,]))

#11
def palindrome(word):
    s = word.lower()
    
    return s == s[::-1]

print(palindrome("madam"))

#12
def histogram(nums):
    for i in nums:
        print(i * "*")

histogram([4, 9, 7])

#13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    number_to_guess = random.randint(1, 20)
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    attempt = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        attempt += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempt} guesses!")
            break  

guess_the_number()


