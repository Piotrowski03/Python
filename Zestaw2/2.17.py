def sort_alphabetical(line):
    words = line.split()
    sorted_words = sorted(words)
    return sorted_words
def sort_length(line):
    words = line.split()
    sorted_words = sorted(words, key = len,reverse = True)
    return sorted_words
line = 'jabłko ananas gruszka brzoskwinia'
print("sorted in alphabetical order" )
print(sort_alphabetical(line))
print("sorted by lenght of the words")
print(sort_length(line))



