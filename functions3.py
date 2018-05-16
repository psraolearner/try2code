def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a Blanket.\n"
       
        
print "We can just give the function numbers directly:"
cheese_and_crackers(25, 35)
    
    
print "OR, we can use variables from our script:"
amount_of_cheese = 15
amount_of_crackers = 40
    
    
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
    
print "We can even do math inside too:"
cheese_and_crackers(15+45,10+20)
    
print "And we can combine the two,  variable and math:"
cheese_and_crackers(amount_of_crackers+1000,amount_of_cheese+500)
    