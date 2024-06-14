#List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt (www.py4e.com/code3/romeo.txt) containing a subset of Shakespeare’s work.

# Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
wordlist=list()
for line in fh:
    line = line.strip()
    words = line.split()
    for word in words:
        if word in wordlist:
            continue
        else:
            wordlist.append(word)
wordlist.sort()
print(wordlist)