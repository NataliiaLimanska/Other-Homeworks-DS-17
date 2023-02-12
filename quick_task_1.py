import math

a = 1
b = 2
# using temporarily value
temp = a
a = b
b = temp
print (a, b)

# without temporarily variable
x = 5
y = 7
x, y = y, x
print(x, y)

#sum of three numbered number input by user
a=123
first_digit = a//100
last_digit =a%10
second_digit =a%100//10
# print(first_digit,second_digit, last_digit)
print(first_digit + second_digit + last_digit)


#hypotenuse lenght
# from math import sqrt
# print("Input lengths of triangle sides:")
# a = float(input("a: "))
# b = float(input("b: "))
# c = sqrt(a**2 + b**2)
# print("The length of the hypotenuse is:", c )

#credit sum
#a=sum for the certain period
#b=null sum
#p=%
#n - amount of periods
startova_suma = float(input('start_sum: '))
vidsotok = float(input('percentage: '))
n = float(input('period in years: '))

kinzeva_suma=startova_suma*(1 + vidsotok/100)**n
dobutok=kinzeva_suma - startova_suma

print(dobutok)

# Function to calculate the position
# of characters
NUM = 31

def letter_position(str):
    for char in str:
        # Performing AND operation
        # with number 31
        print((ord(char) & NUM), end=" ")

# user code
str = input('enter two letters: ')
letter_position(str)

# x = input('enter a letter: ')
# y = input('enter another letter: ')
# sum_of_chars = lambda i:sum(y-x==abs(ord(i[y])-ord(i[x]))for x in range(len(i))for y in range(x+1,len(i)))
# print(sum_of_chars)