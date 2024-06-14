# Write a program that reads the words in words.txt and stores them as keys in a dictionary. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

fname = input('Enter the file name: ')
openf = open(fname)
textdic = dict()
for line in openf:
    line = line.rstrip()
    words = line.split()
    for word in words:
        textdic[word] = 1
print(textdic)


if 'boring' in textdic:
    print("\n'boring' is a key in the dictionary")