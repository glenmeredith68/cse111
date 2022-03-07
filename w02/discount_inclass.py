#Get the date and time
from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()



#print(day_of_week)
# 

def discount_opportunity(amount):
    return (amount * .9)

def total_calculator(price,quantity):
    return (price * quantity)
    
#unnecessary
if day_of_week == 0:
    weekday_name = 'Monday'
elif day_of_week == 1:
    weekday_name = 'Tuesday'
elif day_of_week == 2:
    weekday_name = 'Wednesday'
elif day_of_week == 3:
    weekday_name = 'Thursday'
elif day_of_week == 4:
    weekday_name = 'Friday'
elif day_of_week == 5:
    weekday_name = 'Saturday'
elif day_of_week == 6:
    weekday_name = 'Sunday'


#test
#print(weekday_name)

subtotal = 0
price = 1
print('You will need to enter the price and quantity of each item.')
while price != 0:
    price = float(input('What is the price of the item? ')) 
    if price != 0:
        quantity = int(input('How many did you get? '))
        subtotal += price * quantity
#subtotal = float(input('What is the subtotal? '))

if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        discounted_subtotal = subtotal * .9
        discount = subtotal * .1
        sales_tax = subtotal *.06
        Total = discounted_subtotal + sales_tax
        print()
        print(f'Today is {weekday_name}, so you qualify for a discount if you spend over $50! ')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Discount: {discount:.2f}')
        print(f'Sales tax: {sales_tax:.2f}')
        print(f'Total: {Total:.2f}')
    else:
        sales_tax = subtotal *.06
        Total = subtotal + sales_tax
        print()
        print(f'Today is {weekday_name}, so you qualify for a discount if you spend over $50! ')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'You are only {50 - subtotal} dollars away from getting 10% off! ')
        print(f'Sales tax: {sales_tax:.2f}')
        print(f'Total: {Total:.2f}')
elif day_of_week == 0 or day_of_week > 2:
    subtotal = round(subtotal, 2)
    sales_tax = subtotal *.06
    Total = subtotal + sales_tax
    print()
    print(f'Today is {weekday_name}, so there is no discount. ')
    print(f'Subtotal: {subtotal:.2f}')
    print(f'Sales tax: {Sales_tax:.2f}')
    print(f'Total: {Total:.2f}')
    