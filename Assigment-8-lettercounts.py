from collections import Counter
counts=Counter(word) # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
for i in word:
    print(i,counts[i])
word = "hippo runs to us!"  
