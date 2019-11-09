# The hello world
print("Hello, I'm  Python")
# The input
# name = input('What is your name?')
# print('Hi, %s.' % name)
# Fibonacci
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
# Arrays
fruits = ['Banana', 'Apple', 'Lime']
load_fruits = [fruit.upper() for fruit in fruits]
print(load_fruits)
print(list(enumerate(fruits)))

numbers = [2, 4, 6, 8, 10]
product = 1
for number in numbers:
    print ("%d * %d" % (product, number))
    product = product * number    
print('The product is: ', product)
# direct operations
print(1/5)
print(2 ** 3)
print(17/3)
print(17 // 3)
