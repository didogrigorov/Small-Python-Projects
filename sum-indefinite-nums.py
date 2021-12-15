s = input("Enter a number or done?: ")
total = 0

while s != "done":
  num = int(s)
  total += num
  s = input("Enter a number or done?: ")
print(total)
