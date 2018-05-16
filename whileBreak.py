"""
name = ""
while True:
    print("Who are you?")
    name = input()
    if name != "Sid":
        continue
    print("Hello, Sid.What is password? (It is fish.)")
    password = input()
    if password == "swordfish":
        break
print("Access granted")

"""

name =''                           # (1)
while name != 'your name':          # (2)
    print('Please type your name.')
    name = input()                  # (3)
print('Thank you!') 