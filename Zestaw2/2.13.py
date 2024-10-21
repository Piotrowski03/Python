def sum_of_letters(line):
    words = line.split()
    number = 0
    for i in range(0, len(words)):
        number += len(words[i])

    return number
line = "lal lala lalala"
print(sum_of_letters(line))
