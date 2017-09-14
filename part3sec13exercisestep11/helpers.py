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


def profile(motifs):
    c = count(motifs)
    size = len(motifs)
    for k in c.keys():
        c[k] = list(map(lambda v: float(v)/float(size), c[k]))
    return c


def consensus(motifs):
    p = profile(motifs)
    size = len(motifs[0])
    s = ""
    for i in range(size):
        picked = None
        val = 0
        for c in 'ACGT':
            if p[c][i] > val:
                picked = c
                val = p[c][i]
        s = s + picked
    return s

def score(motifs):
    cons = consensus(motifs)
    score = 0
    size = len(motifs[0])
    for motif in motifs:
        for i in range(size):
            if motif[i] != cons[i]:
                score = score + 1
    return score