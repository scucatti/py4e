# Chapter 3: Conditional execution

# Exercise 1: Rewrite your 'pay computation' code to give the employee 1.5 times
# the hourly rate for hours worked above 40 hours.

hours = input('Enter hours: ')
rate = input('Enter rate: ')

hours = float(hours)
rate = float(rate)

if hours > 40 :
    regular =  hours * rate
    additional = (hours - 40)*(rate*0.5)
    pay = regular + additional
else :
    pay = hours * rate

print('Pay:',pay)
