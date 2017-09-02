# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def pattern_matching(pattern, genome):
    output = []
    text_size = len(genome)
    pattern_size = len(pattern)
    for i in range(0, text_size - pattern_size + 1):
        chop = genome[i:i + pattern_size]
        if chop == pattern:
            output.append(i)
    return output


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(' '.join([str(i) for i in pattern_matching(lines[0],lines[1])]))