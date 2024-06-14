# Write a program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes after typing "done".

numbers = list()
while True:
    # user input
    ui = input("Enter a number or 'done': ")
    if ui == 'done':
        break
    try:
        number = float(ui)
    except :
        print("Invalid input")
        continue
    numbers.append(number)    
print('Maximum:',max(numbers))
print('Minimum:',min(numbers))