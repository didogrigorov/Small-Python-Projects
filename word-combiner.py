#first list of words
words_number = int(input())
phrases_one = input()
phrases_list_one = []

phrases_list_one.append(phrases_one)

while len(phrases_list_one) < words_number:
    phrases_one = input()
    phrases_list_one.append(phrases_one)

print(phrases_list_one)

#second list of words

words_number_2 = int(input())
phrases_two = input()
phrases_list_two = []

phrases_list_two.append(phrases_two)

while len(phrases_list_two) < words_number_2:
    phrases_two = input()
    phrases_list_two.append(phrases_two)

print(phrases_list_two)

for i in phrases_list_one:
    for j in phrases_list_two:
        print(f"{i} {j}")
