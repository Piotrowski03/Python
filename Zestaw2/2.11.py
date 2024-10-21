import string


def underline_between(word):
    new_word = word[0]
    for i in range (1, len(word)  ):
        new_word = new_word + "_" + word[i]
    print(new_word)


underline_between("word")
