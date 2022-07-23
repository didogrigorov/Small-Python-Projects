import re
input_string = input()
number_words = int(input())
count_dictionary = {}
ideal_relevancy = {}
i = 0

#add keywords to dictionaries and calculate mentions, calculate ideal relevancy if keyword mentioned at least once!
while i < number_words:
    searched_word = input()
    pattern = fr'\b{searched_word}\b'
    matches = re.findall(pattern, input_string, flags=re.I)
    if matches:
        if matches[0] not in count_dictionary:
            count_dictionary[searched_word] = len(matches)
        if matches[0] not in ideal_relevancy:
            ideal_relevancy[searched_word] = len(matches)
    else:
        count_dictionary[searched_word] = 0
        ideal_relevancy[searched_word] = 1
    i+=1

#show a list of all keyword mentions
for word,count in count_dictionary.items():
    if count == 0:
        print(f"Keyword: {word} | Mentions: {count} -> Mention keyword at least once!")
    else:
        print(f"Keyword: {word} | Mentions: {count}")

#calculate current average value
current_score = 0
for val in count_dictionary.values():
    current_score += val
print(f"Current score: {current_score * 1}%")

#calculate ideal average value
ideal_score = 0
for values in ideal_relevancy.values():
    ideal_score += values
print(f"Ideal score must be at least: {ideal_score * 1}%")

#final result for the content
if current_score < ideal_score:
    print("Lower relevancy")
elif ideal_score == current_score:
    print("Good relevancy")
