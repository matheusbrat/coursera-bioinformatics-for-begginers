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


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
A = [float(c) for c in lines[0].split()]
C = [float(c) for c in lines[1].split()]
G = [float(c) for c in lines[2].split()]
T = [float(c) for c in lines[3].split()]
Profile = {'A':A,'C':C,'G':G,'T':T}
Dna = lines[4:]
print('\n'.join(motifs(Profile,Dna)))