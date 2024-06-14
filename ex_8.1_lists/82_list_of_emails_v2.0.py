#another approach to the previous code, using a guardian statement

fname = input("Enter file name: ")
readfile = open(fname)
count = 0
for line in readfile:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0]!='From':
        continue
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")