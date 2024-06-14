# Write a program to read through a mail log, build a histtogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

# import file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# create the dictionary for counting the number of sent emails from each email address
counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        for word in words:
            if '@' in word:
                counts[word] = counts.get(word, 0) + 1

# Retrieve the list of emails sent by each address                
for key in counts:
    print(key, counts[key])
