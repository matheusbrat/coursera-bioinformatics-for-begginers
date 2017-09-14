def hamming_distance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist = dist + 1
    return dist
