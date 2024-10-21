def count_of_zeros(number):
    line = str(number)
    counter = 0
    for i in range(0, len(line)):
        if (line[i] == "0"):
            counter += 1
    return counter

number = 122333004533005350
print(count_of_zeros(number))
