# Name: Haider Shoaib
# Date: Thursday June 8, 2018
# File Name: Assign6.py
# Description: This program simulates speed dialing on a telephone. A total of
# 10 numbers can be stored in the speed dial list. 


# Import time module
import time

# define menu function
def menu():
    # Error check the user input
    while True:
        try:
            # Output menu option
            print('*'*80)
            print('\nMenu Options\n')
            print('1 - Enter a number')
            print('2 - Dial a number')
            print('3 - Exit')

            option = int(input('\nEnter option: '))

            if option in[1, 2, 3]:
                break

            else:
                print('\nPlease enter 1, 2 or 3 to continue!')


        except:
            print('\nPlease enter 1, 2 or 3 to continue!')

    # Return the menu option that the user chooses
    return option


# Define location function
def get_location():
    while True:
        try:
            # Get the speed diallocation from user and error check
            location = int(input('Enter speed-dial location (0 to 9): '))

            if location >= 0 and location <= 9:
                return location

            else:
                print('Please enter a number between 0 and 9.')

        # Output error message if location number is out of range
        except:
            print('Please enter an appropiate number between 0 and 9.')
        


# define enter function
def enter(numbers):
    phone_num = False

    # Call location function in enter numbers function
    while True:
        location = get_location()

        #Check if there is an existing number in the chosen location
        if numbers[location - 1] != '':
            choice = input('There is an existing number here, would you like\
to replace it? (Y/N): ')

            if choice == 'Y':
                break

            else:
                print('\nPlease choose another location\n')

        else:
            break
                
    while True:
        # Get the phone number from the user
        num = input('Enter phone number: ')

        # Error check the number
        if len(num) == 12:
            for x in range(12):
                if num[3] == '-' and num[7] == '-':
                    if num[x] in('0123456789'):
                        phone_num = True

                    else:
                        phone_num = False

            # add the phone number to the list
            if phone_num:
                numbers[location - 1] = num
                return numbers

            else:
                print('Please enter a number in the format: xxx-xxx-xxxx')
                
        # Output error message if length of phone number is incorrect
        else:
            print('Please enter a number in the format: xxx-xxx-xxxx')
    

# define dial function
def dial(numbers):
    # Ask user which speed dial number to dial
    num_choice = int(input('Enter speed-dial number to dial (0 to 9): '))

    #Output message if there is no stored number
    if numbers[num_choice - 1] == '':
        print('\nThere is no current number stored in this location.')
        

    else:
        # Simulate a dialing a phone number
        dialing = dial_simulation()
        print(' ', numbers[num_choice - 1], '\n', sep = '')


# Define the dial simulation function
def dial_simulation():
    # Output the dialing dots
    print('Dialing', end = '')
    for i in range(3):
        time.sleep(1)
        print('.', end = '')


##################
## MAIN PROGRAM ##
##################


# Initialize the list of empty numbers
numbers = ['']*10

# Output welcome message
print(' '*25, 'Welcome to Speed Dial!')

# loop entire program 
while True:
    # Call the menu function
    user_opt = menu()

    if user_opt == 3:
        break
       
        
    elif user_opt == 1:
        # Call the enter function
        upd_list = enter(numbers)

    else:
        # Call the dial function
        dial(numbers)
        time.sleep(2)
        

# Output the exiting message
print('\nThanks for using speed dial!')
