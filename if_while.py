"""
name = ''
while not name: #(1)
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests >0: #(2)
    print('Be sure to have enough room for all your guests.') #(3)
print('Done')
"""
name = ""
while not name:
    print("Enter your name")
    name = str(input("> "))
print("How many guests will you have?")
numOfGuests = input("> ")
if numOfGuests:
    print("Be sure to have enough room for all your guests.")
print("Done.")

"""   
name = ''
while not name: #(1)
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests: #(2)
    print('Be sure to have enough room for all your guests.') #(3)
print('Done')
"""