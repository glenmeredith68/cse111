import math

items = int(input('How many items do you have? ')) 
items_per_box = int(input('How many items per box? '))
boxes = math.ceil(items / items_per_box)
print(f'Looks like you will need {boxes} boxes. ')