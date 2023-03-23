point_arr = input().split()
freezing_point = int(point_arr[0])
boiling_point = int(point_arr[1])

while True:
    current_point = int(input())
    if current_point == -999:
        break
    elif not freezing_point <= current_point <= boiling_point:
        print("Alert!")
        break
    else:
        print("Nothing to report")
