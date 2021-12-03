# INSTRUCTION
# In 1 line we enter the text
# In 2 line - what you need to find
import re

file = open("test.txt", "a")
file.write(input())
file.close()

frequency = {}
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
search = input()
match_pattern = re.findall(search, text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

print("Analyzed accepted")
print("It was searched:", search)
print("Matches:", frequency[word])
