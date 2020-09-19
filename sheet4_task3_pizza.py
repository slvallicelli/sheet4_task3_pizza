toppings = ''
topping = ''

print('Enter "quit" to exit the program')

while True:
    topping = input("Which topping should be put on your pizza? ")
    if topping != 'quit':
        toppings = toppings + ' ' + topping
        print("Excellent choice! Your pizza now contains" + toppings)
        continue
    print("Expect your pizza" + toppings + " delivered in 10 minutes.")
    break


