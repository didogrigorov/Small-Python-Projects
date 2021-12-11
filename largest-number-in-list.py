numbers = input("Input a list of student scores ").split()
for n in range(0, len(numbers)):
  numbers[n] = int(numbers[n])

max_scores = numbers[0]

for item in numbers:
  if item > max_scores:
      max_scores = item
print(max_scores)
