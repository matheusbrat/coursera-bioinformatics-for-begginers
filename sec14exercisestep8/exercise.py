# Copy your PatternMatching function below this line.

# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]                   # store the genome as 'v_cholerae'


# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions
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

print(pattern_matching("CTTGATCAT",  v_cholerae))

# print the positions variable