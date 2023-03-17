year = int(input())
result = None
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = True
        else:
            result = False
    else:
        result = True
else:
    result = False

if result:
    print(f'{year}년은 윤년입니다.')
else:
    print(f'{year}년은 평년입니다.')
