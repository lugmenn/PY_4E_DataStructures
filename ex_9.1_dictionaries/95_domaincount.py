# Write a program that records the domain name (instead of the address) where the message was sent from and the number of emails that were sent from each of those domains.


# import file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print('File cannot be opened: ', name)
    exit()

# dictionary with the domains of the received emails 
domains = dict()
for line in handle:
    if line.startswith('From '):
        # extracting the email and the domain from the line
        em = line.split()[1]
        dm = em.split(@)[1]
        # adding it to the dictionary and counting its occurence
        domains[dm] = domains.get(dm, 0) + 1

for dm in domains:
    print(dm, domains[dm])