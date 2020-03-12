# Chapter 8: Lists

# Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt.
# Write a program to open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list.
# If the word is not in the list, add it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

fname = input('Enter a file: ')
fhandle = open(fname)

words = list()
final = list()

#creating a list with the text words
for line in fhandle :
    line = line.rstrip() # remove blank spaces
    wds = line.split() # split the line into words
    words = words + wds

# creating a list without repeated words
for word in words :
     if word not in final :
         final.append(word)

final.sort()

print(final)
