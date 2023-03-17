input_num = int(input())
result = str(input_num)

if input_num >= 10**18:
    result = str(input_num // 10**18) + 'E'
elif input_num >= 10**15:
    result = str(input_num // 10**15) + 'P'
elif input_num >= 10**12:
    result = str(input_num // 10**12) + 'T'
elif input_num >= 10**9:
    result = str(input_num // 10**9) + 'G'
elif input_num >= 10**6:
    result = str(input_num // 10**6) + 'M'
elif input_num >= 10**3:
    result = str(input_num // 10**3) + 'K'

print(f'{result}')
