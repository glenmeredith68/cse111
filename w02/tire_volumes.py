import math
import time
from datetime import datetime
loop = 'Y'
tires = 0
while loop == 'Y':
    print('Welcome to the tired volume finder. Oh did I say tired? I meant tire. ')
    print('Let\'s get started. ')
    print()
    w = int(input('What is the width of the tire in milimeters? '))
    print()
    a = int(input('What is the aspect ratio of the tire? '))
    print()
    d = int(input('What is the diameter of the wheel in inches? '))
    # volume = (math.pi*w**2*a)
    # volume = (math.pi * w**2 * a*(w * a+ 2540 * d)) / 10000000000
    volume = (math.pi * math.pow(w,2) * a*(w * a+ 2540 * d)) / 10000000000

    print()
    print('Hmmm let me think........')
    print('Okay, I\'ve got it!')
    print()
    print(f'The volume of the tire is {volume:.2f} liters. ')

    # Add w02 Prove
    print()
    now = datetime.now()
    # print(now)

    # with open('volumes.txt', 'at') as volumes_file:

    #     print(now, )

    volumes = open('w02/volumes.txt', 'a')
    volumes.write(f'\n{now.date()}, {w}, {a}, {d}, {volume:.2f}')
    volumes.close()

    # see if they want to keep going
    tires += 1
    loop = input('Do you want to calculate the volume of another tire? (Y/N) ')
    
print()
print(f'Thanks for stopping by today! You got the volume of {tires} tires! ')