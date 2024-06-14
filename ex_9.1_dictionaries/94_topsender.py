# Figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop

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
                
# Get only the email address with the most sent emails
topsender = None
mostemails = None

for key, values in counts.items():
    if mostemails is None or values > mostemails:
        mostemails = values
        topsender = key
        
print(topsender, mostemails)