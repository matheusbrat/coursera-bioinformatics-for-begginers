def pattern_count(pattern, text):
    count = 0 # output variable
    text_size = len(text)
    pattern_size = len(pattern)
    for i in range(0, text_size-pattern_size+1):
        chop = text[i:i+pattern_size]
        if chop == pattern:
            count = count + 1
    return count


def improved_symbol_array(genome, symbol):
    size = len(genome)
    extended_genome = genome + genome[0:size//2]
    r = {}
    r[0] = pattern_count(symbol, extended_genome[0:size//2])
    for i in range(1, size):
        r[i] = r[i-1]
        if extended_genome[i-1] == symbol:
            r[i] = r[i] - 1
        if extended_genome[i+(size//2)-1] == symbol:
            r[i] = r[i] + 1
    return r