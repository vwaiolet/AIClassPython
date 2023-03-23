def sumOfDigits(num):
    arr = []
    num = str(num)
    for ch in num:
        arr.append(ch)

    result = 0
    for i in arr:
        result += int(i)

    return result

print(sumOfDigits(643))
print(sumOfDigits(47253))
