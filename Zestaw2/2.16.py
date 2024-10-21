def switch_the_gvm(line):
    new_line = line.replace("GvR","Guido van Rossum")
    return new_line

line = "bardzo GvR cie widzieć kolego GvR"
print("Before: " + line)

print("After: " + switch_the_gvm(line))
