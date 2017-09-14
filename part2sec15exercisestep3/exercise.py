def hamming_distance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist = dist + 1
    return dist



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(hamming_distance(lines[0],lines[1]))