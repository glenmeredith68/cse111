"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
print()
print('So, sounds like you want to strengthen your heart stronger?')
print()
print('When exercising to strengthen your heart, try to keep your heart rate between 65% and 85% of your heart\'s maximum rate for 20 minutes or longer.')
print()
age = int(input('So! How old are you? '))
print()
print(f'Okay, you look pretty young for a {age} year old. ')
max_rate = 220 - age
sixty_five = max_rate * .65
eighty_five = max_rate * .85
print(f'So your max heart rate is {max_rate}, but you don\'t need to work that hard to strengthen your heart. To strengthen your heart you should try to keep your heart rate between {sixty_five:.0f} and {eighty_five:.0f} beats per minute. ')
print()
print('What\'s that you say? You\'re exercising right now? ')
duration = int(input('How long (in minutes) have you been exercising for? '))
current_rate = int(input('Okay then what is your current heart rate? '))
print()
if current_rate > sixty_five and current_rate < eighty_five and duration >= 20:
    print('Sweet! You\'re on the way to a healthy heart! ')
elif current_rate > sixty_five and current_rate < eighty_five and duration < 20: 
    print('Keep it up a bit longer and you\'ll be getting heart healthy in no time!')
else:
    print(f'That\'s not bad, but in order to get your heart where it needs to be, try to keep your heart rate between {sixty_five:.0f} and {eighty_five:.0f} beats per minute for 20 minutes or more. :) ')
