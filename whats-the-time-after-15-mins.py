hours = int(input())
minutes = int(input())

sum_minutes = minutes + 15

if minutes < 45:
    print(f"{hours}:{sum_minutes}")
elif minutes >= 45 and minutes < 55 and hours == 23:
    print(str(0) + ':' + '0' + str(sum_minutes - 60))
elif minutes >= 55 and hours == 23:
    print(str(0) + ':' + str(sum_minutes - 60))
elif minutes >= 45 and minutes < 55:
    print(str(hours + 1) + ':' + '0' + str(sum_minutes - 60))
elif minutes >= 55:
    print(str(hours + 1) + ':' + str(sum_minutes - 60))
