# Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week

# import file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print('File cannot be opened: ', name)
    exit()

#dictionary with the day of the week
days = dict()
for line in handle:
    if line.startswith('From '):
        # extracting the third word as day
        day = line.split()[2]
        # adding it to the dictionary and counting its occurence
        days[day] = days.get(day, 0) + 1

print(days)