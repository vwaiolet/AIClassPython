result = 0

while True:
    input_num = int(input())
    if input_num < 0:
        break
    else:
        result += input_num

print(result)
