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


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
Text = lines[0]
k = int(lines[1])
A = [float(c) for c in lines[2].split()]
C = [float(c) for c in lines[3].split()]
G = [float(c) for c in lines[4].split()]
T = [float(c) for c in lines[5].split()]
Profile = {'A':A, 'C':C, 'G':G, 'T':T}
print(pmpp(Text,k,Profile))