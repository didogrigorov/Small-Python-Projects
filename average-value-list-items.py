average = input("Input a list of student heights ").split()
for n in range(0, len(average)):
  average[n] = int(average[n])

height = 0
elements = 0
for item in average:
  height += item
  elements += 1

print(height / elements)
