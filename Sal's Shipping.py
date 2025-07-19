# imports
import time

# greeting the user
print("\nWelcome to Sal's Shipping! Let's find the best way to ship your package.")
time.sleep(2)
print("We offer three shipping options: Ground Shipping, Premium Ground Shipping, and Drone Shipping. \n")
time.sleep(2)

# define the package weight
weight = input('Enter the weight of the package in pounds: ')

# validate user input for weight
while True:
    try:
        weight = float(weight)
        if weight < 0:
            weight = input('\nPlease enter a valid weight (must be positive): ')
        else:
            break
    except ValueError:
        weight = input('\nPlease enter a valid number for weight: ')

# define ground shipping price, charged by weight
if weight <= 2:
  ground_shipping_price = 1.5 * weight + 20
elif weight > 2 and weight <= 6:
  ground_shipping_price = 3 * weight + 20
elif weight > 6 and weight <= 10:
  ground_shipping_price = 4 * weight + 20
elif weight > 10:
  ground_shipping_price = 4.75 * weight + 20
else:
  print('\n Please enter a valid weight')

# define premium ground shipping, not charged by weight
ground_shipping_premium = 125

# define drone shipping rateds charged by weight
if weight <= 2:
  drone_shipping_price = 4.5 * weight
elif weight >2 and weight <= 6:
  drone_shipping_price = 9 * weight
elif weight > 6 and weight <= 10:
  drone_shipping_price = 12 * weight
elif weight > 10:
  drone_shipping_price = 14.25 * weight
else:
  print('\nPlease enter a valid weight')

# define which is the cheapest way to ship an item
if ground_shipping_price < ground_shipping_premium and ground_shipping_price < drone_shipping_price:
  cheapest_option = 'Your cheapest option to ship this item is with ground shipping. Total cost: ${:.2f} \n'.format(ground_shipping_price)
elif ground_shipping_premium < ground_shipping_price and ground_shipping_premium < drone_shipping_price:
  cheapest_option = 'Your cheapest option to ship this item is with premium ground shipping. Total cost: ${:.2f} \n'.format(ground_shipping_premium)
elif drone_shipping_price <= ground_shipping_price and drone_shipping_price <= ground_shipping_premium:
  cheapest_option = 'Your cheapest option to ship this item is via drone shipping. Total cost: ${:.2f} \n'.format(drone_shipping_price)
else:
  cheapest_option = '\nPlease enter a valid weight '

print(cheapest_option)
time.sleep(2)

more_items = input("Thank you for using Sal's Shipping! Do you have another package to ship? (yes/no) \n").strip().lower()
while more_items not in ['yes', 'no']:
   print('Please answer with "yes" or "no". \n')
   more_items = input("Do you have another package to ship? (yes/no)  ").strip().lower()

while more_items == 'yes':
    weight = input('Enter the weight of the package in pounds: ')
    
    # validate user input for weight
    while True:
        try:
            weight = float(weight)
            if weight < 0:
                weight = input('\nPlease enter a valid weight (must be positive): ')
            else:
                break
        except ValueError:
            weight = input('\nPlease enter a valid number for weight: ')
    
    # repeat the shipping cost calculations
    if weight <= 2:
        ground_shipping_price = 1.5 * weight + 20
    elif weight > 2 and weight <= 6:
        ground_shipping_price = 3 * weight + 20
    elif weight > 6 and weight <= 10:
        ground_shipping_price = 4 * weight + 20
    elif weight > 10:
        ground_shipping_price = 4.75 * weight + 20
    else:
        print('\nPlease enter a valid weight')
    
    ground_shipping_premium = 125
    
    if weight <= 2:
        drone_shipping_price = 4.5 * weight
    elif weight >2 and weight <= 6:
        drone_shipping_price = 9 * weight
    elif weight > 6 and weight <= 10:
        drone_shipping_price = 12 * weight
    elif weight > 10:
        drone_shipping_price = 14.25 * weight
    else:
        print('\nPlease enter a valid weight')
    
    # define which is the cheapest way to ship an item
    if ground_shipping_price < ground_shipping_premium and ground_shipping_price < drone_shipping_price:
        cheapest_option = 'Your cheapest option to ship this item is with ground shipping. Total cost: ${:.2f} \n'.format(ground_shipping_price)
    elif ground_shipping_premium < ground_shipping_price and ground_shipping_premium < drone_shipping_price:
        cheapest_option = 'Your cheapest option to ship this item is with premium ground shipping. Total cost: ${:.2f} \n'.format(ground_shipping_premium)
    elif drone_shipping_price <= ground_shipping_price and drone_shipping_price <= ground_shipping_premium:
        cheapest_option = 'Your cheapest option to ship this item is via drone shipping. Total cost: ${:.2f} \n'.format(drone_shipping_price)
    else:
        cheapest_option = '\nPlease enter a valid weight '
    
    print(cheapest_option)
    time.sleep(2)
    
    # Ask if user wants to ship another package
    more_items = input("Do you have another package to ship? (yes/no)  ").strip().lower()
    while more_items not in ['yes', 'no']:
        print('Please answer with "yes" or "no".')
        more_items = input("Do you have another package to ship? (yes/no) ").strip().lower()

print("\nThank you for using Sal's Shipping! We look forward to seeing you again soon!\n")

