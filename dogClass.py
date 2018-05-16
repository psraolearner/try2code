class Dog:
    
    """A simple class for defining a Dog."""
    
    def __init__(self,name,age):
        """Constructor """
        """initialize name and age attributes"""
        self.name=name
        self.age=age

    def sit(self):
        """Simulate a Dog sitting in response to a command."""
        print(self.name.title()+ " is sitting now")

    def roll_over(self):
        """Simulate rolling over in response to a command ."""
        print(self.name.title() + " is rolled over now")
        
    pass
        
#Making an instance from a class       
D=Dog("jerry",2)
myDog= Dog("sid",3)

#Accessing attributes or parameters
print("My Dog name is "+ myDog.name.title()+".")
print(myDog.name.title()+ " is "+ str(myDog.age)+ " years old.")

print("\n")

#Calling methods
D.sit()
D.roll_over()
myDog.sit()
myDog.roll_over()
