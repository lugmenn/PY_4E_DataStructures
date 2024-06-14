#Write a program to prompt for a file name, and search for lines of the form: "X-DSPAM-Confidence: 0.8475"

#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line.

#When you reach the end of the file, print out the average spam confidence
    
fname = input('Enter the file name: ')
total = 0
count = 0
try:
    readf = open(fname)
except:
    print('File name not found:', fname)
    exit()
for line in readf:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        confidence = float(line[20:])
        total = total + confidence
        count = count + 1
print('Average SPAM confidence:', total/count)
