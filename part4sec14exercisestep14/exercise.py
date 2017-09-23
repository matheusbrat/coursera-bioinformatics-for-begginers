import random

def random_motifs(dna, k, t):
    r = []
    for s in dna:
        start = random.randint(0, t-1)
        r.append(s[start:start+k])
    return r


def count_with_pseudo(motifs):
    h = {'A': [], 'C': [], 'G': [], 'T': []}
    size = len(motifs[0])
    for c in range(0, size):
        for k in h.keys():
            h[k].append(1)

    for motif in motifs:
        for c in range(size):
            h[motif[c]][c] = h[motif[c]][c] + 1

    return h


def consensus(motifs):
    p = profile_with_pseudo(motifs)
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


def profile_with_pseudo(motifs):
    c = count_with_pseudo(motifs)
    size = len(motifs) + 4
    for k in c.keys():
        c[k] = list(map(lambda v: float(v)/float(size), c[k]))
    return c

def random_motifs(dna, k, t):
    r = []
    for s in dna:
        start = random.randint(0, t-1)
        r.append(s[start:start+k])
    return r

def pr(text, pro):
    prob = 1
    for i in range(len(text)):
        prob = float(prob) * float(pro[text[i]][i])
    return prob


def pmpp(text, k, profile):
    prob = -1
    ppt = None
    for i in range(len(text)-k+1):
        pt = text[i:i + k]
        mp = pr(pt, profile)
        if mp > prob:
            prob = mp
            ppt = pt
    return ppt

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

def gs(dna, k, t, n):
    motifs = random_motifs(dna, k, t)
    # print(len(motifs), len(dna))
    best_motifs = motifs
    for j in range(0, n):
        i = random.randint(1, t-1)
        del motifs[i]
        # print(motifs)
        profile_matrix = profile(motifs)
        # print(profile_matrix)
        motifs.insert(i, pmpp(dna[i], k, profile_matrix))
        # print(motifs)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


dna = """GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC
CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG
ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC
GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC
GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG
CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA
GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA
GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG
GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG
TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"""

a = gs(dna.split('\n'), 15, 10, 20)
print(a)
print(score(a))