# Chapter 2: Variables, expressions, and statements

#Exercise 3: Write a program to prompt the user for hours and rate per hour
# to compute gross pay.

hours = input('Enter hours: ')
rate = input('Enter rate: ')

pay = float(hours) * float(rate)

print('pay:', pay)
