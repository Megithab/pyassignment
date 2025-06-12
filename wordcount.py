text = input("Enter a sentence or paragraph: ")

words = text.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

total_words = len(words)
most_frequent = max(word_count, key=word_count.get)

print("Total words:", total_words)
print("Word frequencies:")

for word, count in word_count.items():
    print(word, ":", count)

print("Most frequent word:", most_frequent)
