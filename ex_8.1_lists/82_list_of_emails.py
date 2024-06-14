# Write a program to read through the mail box data and when you find line that starts with “From”, and print who sent the message. Then you will also count the number of From (not From:) lines and print out a count at the end.

fname = input("Enter file name: ")
readfile = open(fname)
count = 0
for line in readfile:
    if not line.startswith('From:'): 
        continue
    else:
        words = line.split()
        print(words[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
