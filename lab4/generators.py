#1
def square(n):
    for i in range(1, n+1):
        yield i **2
n = int(input("Enter a number: ")) 
sqr = square(n)
for s in sqr:
    print(s, end=", ")  


#2
def even(n):
    for i in range(0, n+1):
        if i%2==0:
            yield i
n = int(input("Enter a number: "))
ev = even(n)
for e in ev:
    print(e, end=", ")

#3
def divisible(n):
    for i in range(0, n+1):
        if i%3 ==0 and i%4==0:
            yield i
n = int(input("Enter a number: "))
div = divisible(n)
for d in div:
    print(d, end=", ")

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sq = squares(a, b)
for s in sq:
    print(s, end=", ")

#5
def count(n):
    while n >= 0:
        yield n
        n-=1
n = int(input("Enter a number: "))
co = count(n)
for c in co:
    print(c, end=", ")