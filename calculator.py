def menu():
    print('Choices:\n1. Addition\nMore coming soon!')

print('Welcome to the best calculator!\n')
menu(), print("\n")

choice = int(input('Choice: '))
if choice < 1 or choice > 1:
    print('Invalid Selection')

if choice == 1:
    x = int(input('Choose your first number: '))
    y = int(input('Choose your second number: '))

#Addition
if choice == 1:
    print('{} + {} = '.format(x, y))
    print(x+y)
