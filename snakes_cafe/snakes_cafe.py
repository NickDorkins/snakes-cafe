# DONE When run, the program should print an intro message and the menu for the restaurant
# DONE The restaurant’s menu should include appetizers, entrees, desserts, and beverages.
# DONE The program should prompt the user for an order
# DONE When a user enters an item, the program should print an acknowledgment of their input
# DONE The program should tell the user how to exit
# DONE Create "quit" functionality 
# DONE The program’s content should match included sample exactly
# DONE Actually, there’s one tiny spot that should be different - see if you can spot it.
# DONE The > character represents user input line and should be printed out with a trailing space.



print('*'*38)
print ('**' + '  ' + 'Welcome to Snakes Cafe!' + ' '*9 + '**')
print ('**' + '  ' + 'Please see our menu below.' + '      ' + '**')
print ('**' + '  '*17 +  '**')
print ('**' + ' To quit at any time. type "quit" ' + '**')
print('*'*38)

print(
  """
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

  """
)
print('*'*38)
print('**' + '  What would you like to order? ' + '  **')
print('*'*38)

orders = {
    'wings': 0,
    'cookies': 0,
    'spring rolls': 0,
    'salmon': 0,
    'steak': 0,
    'meat tornado': 0,
    'a literal garden': 0,
    'ice cream': 0,
    'cake': 0,
    'pie': 0,
    'coffee': 0,
    'tea': 0,
    'unicorn tears': 0,
}

# While Loop
while True:
# Define global variable
  user_input = input('> ')
# Validate quit or order (boolean)
  if user_input == 'quit':
    break
# Get key value pair
  else:
# Increment value of user input
    orders[user_input] += 1

#get key value pairs 
  for key, value in orders.items():
# check to see if 1 item is ordered
    if value == 1:
      print('** 1 order of ' + user_input + ' have been added to your meal **')
# check to see if more than 1 item is ordered
    elif value > 1:
# define iteration as a variable that converts to a string
      qty = str(value)
      print('** ' + qty + ' orders of ' + key + 'have been added to your meal **')
      user_input
    else:
      continue
    




# print(orders[user_input])

    #if __name__ == '__main__':
     # menu()