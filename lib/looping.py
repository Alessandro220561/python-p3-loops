#!/usr/bin/env python3

def happy_new_year():
    countdown = 10

    while countdown > 0:
        print(countdown)
        countdown -= 1
    
    print("Happy New Year!")
    

def square_integers(int_list):
    squared_integers = [int ** 2 for int in int_list]
    return squared_integers

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)