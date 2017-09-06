# Input:  A String Genome
# Output: Skew(Genome)
def Skew(genome):
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


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
skew = Skew(sys.stdin.read().strip())
print(' '.join([str(skew[i]) for i in sorted(skew.keys())]))