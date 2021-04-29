# import math
# print(math)
# signal_power = 2
# noise_power =344
# ratio = signal_power / noise_power
# decibels = 10 * math.log10(ratio)
# radians = 0.7
# height = math.sin(radians)

# import math 
# r = int(input("Please enter a radius"))
# sphere = (4/3)*math.pi* r**3
# print(sphere)
def bookprice():
    cover_price = 24.95


    units = int(input("Please enter the number of units you want to buy"))
    if units > 1:
        shipping_cost = 3 + (0.75 * (units-1))
    elif units == 1:
        shipping_cost = 3
    else:
        print("Please enter a number betwe 1 and infinity")
    response = ['Y', 'N']
    
    
      
    running = True
    while running:    
        confirm_bookstore = input("Are you a bookstore owner?" 'Y OR N?')
        if confirm_bookstore in response:
            if confirm_bookstore == 'Y':
                print("Holler")
                new_cover_price = 0.4*cover_price

                total_price = (new_cover_price * units)+shipping_cost   
                print(total_price)
                running = False
                
            else:
                total_price = (cover_price * units)+shipping_cost  
                print(total_price)
                running =False
        else:
            print("Confirm if you are a book store owner or not (Y OR N")
            running =True
            
        
    
        
bookprice()