"""
def user():
    print("Good morning!")
user()


def greet_user(username):
    print("Hello, " +username.title()+ "\nGood Evening")
greet_user("siva")


def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a "+ animal_type.title() + ".")
    print("\nMy "+animal_type+"\'s name is "+ pet_name.title()+".")
    
describe_pet("jimmy")
describe_pet("danny")

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dode cahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("unprinted_designs: "+str(unprinted_designs))
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model.title())

def greet_users(names):

#Print a simple greeting to each user in the list.
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
names = ['siva', 'prasad', 'srinivas']
greet_users(names)


def get_formatted_name(fname,lname):
    fullname = fname + " " +lname
    return fullname.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    fname = input("First name: ")
    if fname == 'q':
        break
    lname = input("Last name: ")
    if lname == 'q':
        break
    formatted_name = get_formatted_name(fname, lname)
    print("\nHello, "+ formatted_name + "!")

def build_person(fname,lname, age = ' '):
    person={"first":fname,"last":lname}
    
    if age:
        person[age] = age 
    return person

musician=build_person("Siva","prasad",age =25)
print(musician)

def make_pizzas(size, *toppings):
    
    print("\n Making a " + str(size) + " inch pizza with following toppings: ")
    for topping in toppings:
        print("-"+ topping.title())
make_pizzas(14,"extra cheese","chicken","pepperoni")
make_pizzas(12,"mushrooms")
"""

def build_profile(first, last, **user_info):

#Build a dictionary containing everything we know about a user.
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile 
user_profile = build_profile('albert', 'einstein', place ='seattle', field='statistics')
print(user_profile)
"""
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""
