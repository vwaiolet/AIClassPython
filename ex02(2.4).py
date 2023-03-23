for i in range(1, 100+1):
    if i % 3 == 0:
        if i % 5 == 0:
            print('피즈 버즈', end=', ')
        else:
            print('피즈', end=', ')
    else:
        if i % 5 == 0:
            print('버즈', end=', ')
        else:
            print(i, end=', ')

print('\n')
for i in range(1, 100+1):
    match(i % 3, i % 5):
        case (0, 0):
            print('피즈 버즈', end=', ')
        case (0, _):
            print('피즈', end=', ')
        case (_, 0):
            print('버즈', end=', ')
        case _:
            print(i, end=', ')