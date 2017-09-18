def pr(text, pro):
    prob = 1
    for i in range(len(text)):
        prob = float(prob) * float(pro[text[i]][i])
    return prob

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
Text = lines[0]
A = [float(c) for c in lines[1].split()]
C = [float(c) for c in lines[2].split()]
G = [float(c) for c in lines[3].split()]
T = [float(c) for c in lines[4].split()]
Profile = {'A':A, 'C':C, 'G':G, 'T':T}
print(pr(Text,Profile))