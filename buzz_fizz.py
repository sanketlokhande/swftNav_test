#!/bin/python
# Code run in python 3.6.1
# Description: A fibonacci generator with few select numbers replaced by string:
#   "Buzz" when F(n) is divisible by 3.
#   "Fizz" when F(n) is divisible by 5.
#   "FizzBuzz" when F(n) is divisible by 15.
#   "BuzzFizz" when F(n) is prime.
#   the value F(n) otherwise.

# usage python buzz_fizz.py
#    input your number when prompted
# Author : Sanket Lokhande Email: slokhande@nevada.unr.edu

import sys

def F(n):
    j=1
    a=[]  # store fibonacci series here
    b=[]  # store substituted series here
    for i in range(n):
        a.append(j)
        j=sum(a[-2:])
    for i in a:
        if not i%3:
            b.append('Buzz')
        elif not i%5:
            b.append('Fizz')
        elif not i%15:
            b.append('FizzBuzz')
        elif isPrime(i)==True:
            b.append('BuzzFizz')
        else:
            b.append(i)
    print ('Fibonacci Series till ' + str(n) + ' = ' + str(a))
    print ('Substituted fibonacci  =  ' + str(b))

def isPrime(number):
    count = 0
    if number == 0 or number == 1:
        return False
    for integer in range(2, 10, 1):
        if number % integer == 0 and number != integer:
            count += 1
    if count == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    if sys.version_info < (3,0):
        raise "Please use python v3.0 or greater"
    else:        
        Num=int(input('Input your number greater than 0: '))
        if Num<0:
            print ("Invalid number")
        else:
            F(Num)
        
