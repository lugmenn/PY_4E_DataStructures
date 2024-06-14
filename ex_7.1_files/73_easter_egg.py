#Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”


fname = input('Enter the file name: ')
count=0
if fname == 'na na boo boo':
    print('Chocolate ounces, sit on that, bounce it, bounce it')
else:
    try :
        readf = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()
    for line in readf:
        if line.startswith('Subject:'):
            count = count + 1
    print('There were', count, 'subject lines in', fname)