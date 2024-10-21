def number_of_words(line):
    words = line.split()
    number = len(words)
    return number

linia = "Siała baba mak, nie wiedziała jak, dziad chciał jej pomóc\n ale nie dopomógł"
liczba = number_of_words(linia)
print(liczba)
