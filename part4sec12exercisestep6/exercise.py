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


def profile_with_pseudo(motifs):
    c = count_with_pseudo(motifs)
    size = len(motifs) + 4
    for k in c.keys():
        c[k] = list(map(lambda v: float(v)/float(size), c[k]))
    return c


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

def motifs(p, dna):
    r = []
    size = len(p['A'])
    for line in dna:
        r.append(pmpp(line, size, p))
    return r

def randomized_motif_search(dna, k, t):
    M = random_motifs(dna, k, t)
    BestMotifs = M
    while True:
        Profile = profile_with_pseudo(M)
        M = motifs(Profile, dna)
        if score(M) < score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
def RepeatedRandomizedMotifSearch(Dna, k, t):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(1000):
        Motifs = randomized_motif_search(Dna, k, t)
        CurrScore = score(Motifs)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    return BestMotifs
import sys
lines = sys.stdin.read().splitlines()
k,t = lines[0].split()
k = int(k)
t = int(t)

print('\n'.join(RepeatedRandomizedMotifSearch(lines[1:],k,t)))