# Write a program to read through a file and print the contents of the file (line by line) all in upper case

fname = input('Enter the file name: ')
try:
    readf = open(fname)
except:
    print('File name not found:', fname)
    exit()
for line in readf :
    line = line.upper().rstrip()
    print(line)