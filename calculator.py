print('Welcome to the best calculator!\n')
endchoice = ""
while endchoice == "":
    def menu():
        print('Choices:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division')

    print("\n")
    menu(), print("\n")

    choice = int(input('Choice: '))
    while choice < 1 or choice > 4:
        print('Invalid Selection')
        choice = int(input('Choice: '))

    if choice >= 1 and choice <= 4 :
        x = int(input('Choose your first number: '))
        y = int(input('Choose your second number: '))

    #Addition
    if choice == 1:
        print('{} + {} ='.format(x,y),x+y)

    #Subtraction
    if choice == 2:
        print('{} - {} ='.format(x,y),x-y)

    #Multiplication
    if choice == 3:
        print('{} * {} ='.format(x,y),x*y)
    #Division
    if choice == 4:
        print('{} / {} ='.format(x,y),x/y)
    print('\n')
    endchoice = input('Press Enter to continue...')
