def hamming_distance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist = dist + 1
    return dist


def approximate_pattern_matching(pattern, text, dist):
    positions = []
    for i in range(0, len(text)-len(pattern)+1):
        s = text[i:i+len(pattern)]
        if hamming_distance(pattern, s) <= dist:
            positions.append(str(i))
    return positions


def approximate_pattern_count(pattern, text, dist):
    return len(approximate_pattern_matching(pattern, text, dist))