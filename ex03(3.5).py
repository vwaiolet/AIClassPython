def read(text):
    ridename, lim = map(str.strip, text.split(':'))
    cmmin = None
    cmmax = None
    if '~' in lim:
        cmmin, cmmax = map(str.strip, lim.split('~'))
        cmmin = cmmin.replace('cm', '')
        cmmax = cmmax.replace('cm', '')
    elif '이상' in lim:
        cmmin = lim.split('cm')[0]

    return ridename, cmmin, cmmax


ridename, cmmin, cmmax = read(input())
print('이름 : ', ridename)
print('하한 : ', cmmin)
print('상한 : ', cmmax)
