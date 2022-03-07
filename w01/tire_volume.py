import math
import time

t1 = time.perf_counter()
print('Welcome to the tired volume finder. Oh did I say tired? I meant tire. ')
print('Let\'s get started. ')
print()
w = int(input('What is the width of the tire in milimeters? '))
print()
a = int(input('What is the aspect ratio of the tire? '))
print()
d = int(input('What is the diameter of the wheel in inches? '))
# volume = (math.pi*w**2*a)
#volume = (math.pi * w**2 * a*(w * a+ 2540 * d)) / 10000000000
t3 = time.perf_counter()
i = 0
while i<1000000:
    volume = (math.pi * math.pow(w,2) * a*(w * a+ 2540 * d)) / 10000000000
    i+=1
t4 = time.perf_counter()
print('Hmmm let me think........')
input('Okay, I\'ve got it!')
print()
print(f'The volume of the tire is {volume:.2f}liters. ')
t2 = time.perf_counter()
print("time: ",t2-t1)
print("time: ",t2-t3)
print("time: ",t4-t3)

