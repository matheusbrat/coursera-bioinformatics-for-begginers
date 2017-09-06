def hamming_distance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist = dist + 1
    return dist


def approximate_pattern_matching(pattern, text, dist):
    positions = []
    for i in range(0, len(text)-len(pattern)+1):
        s = text[i:i+len(pattern)]
        if hamming_distance(pattern, s) <= dist:
            positions.append(str(i))
    return positions


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(' '.join([str(i) for i in approximate_pattern_matching(lines[0],lines[1],int(lines[2]))]))