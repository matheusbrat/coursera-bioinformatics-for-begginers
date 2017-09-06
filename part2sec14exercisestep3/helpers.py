def skew(genome):
    skew = {0: 0}
    genome = ' ' + genome
    for i in range(1, len(genome)):
        if genome[i] == 'G':
            skew[i] = skew[i - 1] + 1
        elif genome[i] == 'C':
            skew[i] = skew[i - 1] - 1
        else:
            skew[i] = skew[i - 1]
    return skew