age = int(input('Whar year were you born? '))
isKorean = None

if age <= 1924:
    print('You\'re the Greatest Generation')
elif age <= 1945:
    print('You\'re the Silent Generation')
elif age <= 1964:
    if 1955 <= age <= 1963:
        isKorean = input('Are you Korean?(y/n)').lower()[0]
        if isKorean == 'y':
            print('You\'re a baby boomer.')
        elif isKorean == 'n':
            print('You\'re the Silent Generation')
elif age <= 1980:
    print('You\'re a Gen X.')
elif age <= 1996:
    print('You\'re a Millennial')
else:
    print('You\'re a Gen Z')
    