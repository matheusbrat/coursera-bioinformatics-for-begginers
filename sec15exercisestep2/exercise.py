# Copy your PatternCount function below here
def pattern_count(pattern, text):
    count = 0 # output variable
    text_size = len(text)
    pattern_size = len(pattern)
    for i in range(0, text_size-pattern_size+1):
        chop = text[i:i+pattern_size]
        if chop == pattern:
            count = count + 1
    return count

# On the following line, create a variable called Text that is equal to the oriC region from T petrophila

text = 'aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaattacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaaacaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggtttctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattcaagattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtatccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggtaagttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaacctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga'

# On the following line, create a variable called count_1 that is equal to the number of times
# that "ATGATCAAG" occurs in Text.

count_1 = pattern_count('ATGATCAAG', text)

# On the following line, create a variable called count_2 that is equal to the number of times
# that "CTTGATCAT" occurs in Text.

count_2 = pattern_count('CTTGATCAT', text)

# Finally, print the sum of count_1 and count_2
print(count_1 + count_2)