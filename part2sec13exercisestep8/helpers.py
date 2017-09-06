def pattern_count(pattern, text):
    count = 0 # output variable
    text_size = len(text)
    pattern_size = len(pattern)
    for i in range(0, text_size-pattern_size+1):
        chop = text[i:i+pattern_size]
        if chop == pattern:
            count = count + 1
    return count


def symbol_array(genome, symbol):
    size = len(genome)
    extended_genome = genome + genome[0:size//2]
    r = {}
    for i in range(0, size):
        r[i] = pattern_count(symbol, extended_genome[i:i+size//2])
    return r