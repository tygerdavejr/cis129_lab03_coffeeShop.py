# Coffee Shop - Lab 03 - CIS 129
# David Vance
# Professor Kevin Chang
#
# Coffee Shop prompts users to input the number of coffee and muffins sold,
# calculates the total price per item, applies a sales tax, and then 
# provides a receipt to include all the values.

##############################################################################
# I learned to program by setting initial values up front.  Having values 
# established here makes it easy to change them in the future.  For example, 
# if the price of a cup of coffee were to increase, I would only need to 
# change the value here instead of every instance it appears in code.
##############################################################################

coffee_price = 5
muffin_price = 4
smoothie_price = 3 # Add Item #3
burrito_price = 5 # Add Item #4

tax_rate = .06

banner_one = "****************************************"
banner_two = "---------"

##############################################################################
# INPUTS
# Prompt the user for the number of coffees and muffins sold
##############################################################################

print (banner_one)

print ('My Coffee and Muffin Shop')
coffee_amount = int (input ('Number of coffees bought? \n'))
muffin_amount = int (input ('Number of muffins bought? \n'))
smoothie_amount = int (input ('Number of smoothies bought? \n')) #input number for Item #3
burrito_amount = int (input ('Number of burritos bought? \n')) #input number for Item #4

print (banner_one, ('\n'))

##############################################################################
# CALCULATIONS
# Determine the total dollar cost for coffees sold, determine the total dollar
# cost for muffins sold, calculate the total amount for all sales, and 
# determine the appropriate singular or plural label for the receipt.
##############################################################################

coffee_total = coffee_price * coffee_amount
muffin_total = muffin_price * muffin_amount
smoothie_total = smoothie_price * smoothie_amount # Determine Item 3 sales
burrito_total = burrito_price * burrito_amount # Determine Item 4 sales

# update to include items 3 and 4
sales_total = coffee_total + muffin_total + smoothie_total + burrito_total 

if coffee_amount == 1:
    coffee_label = 'Coffee'
else:
    coffee_label = 'Coffees'

if muffin_amount == 1:
    muffin_label = 'Muffin'
else:
    muffin_label = 'Muffins'

# Set singular or plural for Item 3
if smoothie_amount == 1:
    smoothie_label = 'Smoothie'
else:
    smoothie_label = 'Smoothies'

# Set singular or plural for Item 4
if burrito_amount == 1:
    burrito_label = 'Burrito'
else:
    coffee_label = 'Burritos'
    
##############################################################################
# OUTPUT
# Print the receipt in accordance with customer requirements. 
# - In some instances the customer did not want a leading space after the $
#   but in other spaces they did.  I converted integer to a string to remove
#   the leading space, else left the print syntax alone to add that space
#   naturally
# - Strip the leading 0 off the displayed sales tax amount if the value is 
#   less than # $1.00
# - Force display of two decimal points for the item amounts
#  
# To strip the 0 I converted the value of sales_tax to a string and then 
# used .lstrip() to cut the leading 0.  This only happens on a tax value
# below $1.00.
#
# To force two digits I used the f"{xxx:.2f}" function to force two decimal 
# places in the display value.  I had to Google both of these.
##############################################################################

print (banner_one)

# convert int to str to display values as requested
coffee_price_text = '$' + str(coffee_price)
muffin_price_text = '$' + str(muffin_price)
smoothie_price_text = '$' + str(smoothie_price) # Set Item 3 Price Text
burrito_price_text = '$' + str(burrito_price)# Set Item 4 Price Text

sales_tax = tax_rate * sales_total
sales_tax_text = str(sales_tax)

# Strip the leading 0 if sales tax less than $1.00
if sales_tax < 1:
    sales_tax_text = sales_tax_text.lstrip('0')

print ('My Coffee and Muffin Shop Receipt')

print (coffee_amount, coffee_label, 'at', coffee_price_text, 'each: $',
       f"{coffee_total:.2f}")
print (muffin_amount, muffin_label, 'at', muffin_price_text, 'each: $',
       f"{muffin_total:.2f}")
print (smoothie_amount, smoothie_label, 'at', smoothie_price_text, 'each: $',
       f"{smoothie_total:.2f}")# Print Item 3 line
print (burrito_amount, burrito_label, 'at', burrito_price_text, 'each: $',
       f"{burrito_total:.2f}")# Print Item 4 line

print (int(tax_rate * 100),'\b% tax: $', sales_tax_text) 

print (banner_two)
print ('Total: $', f"{(sales_tax + sales_total):.2f}")

# Print Thank You line
print ('C|_| Thank you for shopping My Coffee and Muffin Shop ---<@ ')
print (banner_one)






