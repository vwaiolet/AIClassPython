height = 100
gravity = 0.6
i = 1
bound = 10
while i <= bound:
    print(i, round((height * gravity), 4))
    height *= gravity
    i += 1
