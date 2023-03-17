age = int(input('Whar year were you born? '))
if age <= 1924:
    print('You\'re the Greatest Generation')
elif age <= 1945:
    print('You\'re the Silent Generation.')
elif age <= 1964:
    print('You\'re a baby boomer.')
elif age <= 1980:
    print('You\'re a Gen X.')
elif age <= 1996:
    print('You\'re a Millennial')
else:
    print('You\'re a Gen Z')