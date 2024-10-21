#method creating a word from the first letters of the first words from the string
def word_from_first(line):
    words = line.split()
    new_word = words[0][0]
    #i assume first few words are 5
    for i in range(1, 5):
        temp = words[i]
        new_word = new_word + temp[0]

    return new_word

#method creating a  word from the first letters of the few last words from the string
def word_from_last(line):
    words = line.split()
    new_word = words[0][0]
    #again assuming last few words are 5
    for i in range(len(words) - 4, len(words)):
        temp = words[i]
        new_word = new_word + temp[0]

    return new_word

line = "Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line."
print(word_from_first(line))
print(word_from_last(line))
