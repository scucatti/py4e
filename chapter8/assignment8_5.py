# Chapter 8: Lists

# Exercise 5: Write a program to read through the mail box data and
# when you find line that starts with "From", you will split the line into words using the split function.
# We are interested in who sent the message, which is the second word on the From line.

# You will parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a count at the end.

fname = input('Enter a file name: ')
fhand = open(fname)

count = 0

for line in fhand :
    line = line.rstrip() # remove blank spaces
    wds = line.split() # split the line into words

    if len(wds) < 2 :
        continue

    if wds[0] == 'From' :
        count = count + 1
        print(wds[1])

print('There are',count,'lines in the file with From as the first word')
