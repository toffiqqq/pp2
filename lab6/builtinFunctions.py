#1
import functools
list = [1,2,3,4,5,6,7,8,9]
res = functools.reduce(lambda x,y: x*y, list)
print(res)

#2
def count(s):
    upperCase = sum(1 for i in s if i.isupper()) 
    lowerCase = sum(1 for i in s if i.islower()) 
    return upperCase, lowerCase
example = input()
print(count(example))  

#3
def palindrome(word):
    s = word.replace(" ", "").lower()
    return s == s[::-1]

word = input()
print(palindrome(word))

#4
import time
import math
def delay(number, ms):
    seconds = ms/1000
    time.sleep(seconds)
    res = math.sqrt(number)
    print(f"Square root of {number} after {ms} milliseconds is {res}")
num, ms = int(input()), int(input())
delay(num, ms)

#5
def true(tuple):
    return all(tuple)
tuple = (1, 2, 3, 0 ,70)
print(true(tuple))