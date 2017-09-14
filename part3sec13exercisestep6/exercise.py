# Input:  A set of kmers Motifs
# Output: Count(Motifs)
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


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(count(sys.stdin.read().splitlines()))