def reverse_complement(s):
    return complement(s)[::-1]


def complement(s):
    comp = ''
    for c in s:
        if c == 'A':
            comp = comp + 'T'
        elif c == 'T':
            comp = comp + 'A'
        elif c == 'C':
            comp = comp + 'G'
        elif c == 'G':
            comp = comp + 'C'
    return comp


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(reverse_complement(sys.stdin.read().strip()))