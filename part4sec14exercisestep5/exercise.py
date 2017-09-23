# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def normalize(a):
    s = 0
    for v in a.values():
        s = s + v
    for k in a.keys():
        a[k] = float(a[k]) / float(s)
    return a


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(normalize(eval(sys.stdin.read().strip())))