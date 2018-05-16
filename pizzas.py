
def make_pizzas(size, *toppings):
    
    print("\n Making a " + str(size) + " inch pizza with following toppings: ")
    for topping in toppings:
        print("-"+ topping.title())
#make_pizzas(14,"extra cheese","chicken","pepperoni")
#make_pizzas(12,"mushrooms")
