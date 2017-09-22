import random


def random_motifs(dna, k, t):
    r = []
    for s in dna:
        start = random.randint(0, t-1)
        r.append(s[start:start+k])
    return r




### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
k,t = lines[0].split()
k = int(k)
t = int(t)
print('\n'.join(random_motifs(lines[1:],k,t)))