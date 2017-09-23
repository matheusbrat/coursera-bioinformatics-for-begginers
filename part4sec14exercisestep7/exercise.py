import random

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


def pr(text, pro):
    prob = 1
    for i in range(len(text)):
        prob = float(prob) * float(pro[text[i]][i])
    return prob


def normalize(a):
    s = 0
    for v in a.values():
        s = s + v
    for k in a.keys():
        a[k] = float(a[k]) / float(s)
    return a


def pgs(txt, profile, k):
    n = len(txt)
    probabilities = {}
    for i in range(0, n - k + 1):
        probabilities[txt[i:i + k]] = pr(txt[i:i + k], profile)
    probabilities = normalize(probabilities)
    return WeightedDie(probabilities)
