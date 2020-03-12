# Chapter 5: Iterations

# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average

num = 0
max = None
min = None

while True :
    svar = input('Enter a number: ')

    if svar == 'done' :
        break

    try:
        num = float(svar)
    except:
        print('Invalid input')
        continue

    if max == None :
        max = num

    if min == None :
        min = num

    if  num > max :
        max = num
    elif num < min :
        min = num

print('maximum', max, 'minimum', min)
