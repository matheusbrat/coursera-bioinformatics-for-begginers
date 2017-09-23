# first, import the random package
import random

# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(probabilities):
    s = 0
    mod = {}
    for k, v in probabilities.items():
        mod[k] = {'begin': s, 'end': v + s}
        s = v + s
    probabilities = mod
    kmer = '' # output variabl

    r = random.uniform(0, 1)
    for k, v in probabilities.items():
          if r <= v['end'] and r >= v['begin']:
            kmer = k
    # your code here
    return kmer


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys,inspect
dic = {}
lines = sys.stdin.read().splitlines()
it = int(lines[0])
for line in lines[1:]:
    p,kmer = line.split()
    dic[kmer] = float(p)
for i in range(it):
    print(WeightedDie(dic))