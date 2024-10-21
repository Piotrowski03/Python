def longest_word(line):
    words = line.split()
    longest = words[0]
    for i in range(1, len(words)):
        if(len(longest) < len(words[i])):
            longest = words[i]
    print("the longest word is " + longest + " and it has " + str(len(longest)) + " letters")
line = "jestem kurdebele głodny i znudzony"
longest_word(line)
