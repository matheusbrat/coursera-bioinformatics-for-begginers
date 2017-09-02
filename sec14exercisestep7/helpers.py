def pattern_matching(pattern, genome):
    output = []
    text_size = len(genome)
    pattern_size = len(pattern)
    for i in range(0, text_size - pattern_size + 1):
        chop = genome[i:i + pattern_size]
        if chop == pattern:
            output.append(i)
    return output

