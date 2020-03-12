# Chapter 4: Functions

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime
# and create a function called computepay which takes two parameters
# (hours and rate).

def computepay(h, r) :
    if h > 40 :
        regular =  h * r
        additional = (h - 40)*(r*0.5)
        p = regular + additional
    else :
        p = h * r
    return p

hours = input('Enter hours: ')
rate = input('Enter rate: ')

hours = int(hours)
rate = int(rate)

pay = computepay(hours, rate)

print('Pay:',pay)
