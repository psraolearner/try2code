# this one is like yours scripts with argv
def print_two(*args):
    arg1,arg2 =args
    print "arg1: %r, arg2: %r" %(arg1,arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)
    
#this just takes one arguement    
def print_one(arg1):
    print "arg1: %r" %arg1
    
#this one takes no arguements
def print_none():
    print "I got nothin'."
    
        
print_two("Siv","Prasad")
print_two_again("Siv","Prasad")
print_one("First!")
print_none()