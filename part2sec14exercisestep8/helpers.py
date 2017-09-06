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


def min_skew(genome):
    positions = []
    skew_data = skew(genome)
    min_global = 0
    for k, v in skew_data.items():
        if min_global > v:
            min_global = v
            positions = [k]
        elif min_global == v:
            positions.append(k)
    return positions
