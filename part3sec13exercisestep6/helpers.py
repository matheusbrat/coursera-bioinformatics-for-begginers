def count(motifs):
    h = {'A': [], 'C': [], 'G': [], 'T': []}
    size = len(motifs[0])
    for c in range(0, size):
        for k in h.keys():
            h[k].append(0)

    for motif in motifs:
        for c in range(size):
            h[motif[c]][c] = h[motif[c]][c] + 1

    return h
