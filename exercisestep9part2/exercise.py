def frequent_words(text, k):
    frequent_patterns = []
    cdict = count_dict(text, k)
    m = max(cdict.values())
    for i in cdict:
        if cdict[i] == m:
            frequent_patterns.append(text[i:i + k])
    return frequent_patterns

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def pattern_count(pattern, text):
    count = 0 # output variable
    text_size = len(text)
    pattern_size = len(pattern)
    for i in range(0, text_size-pattern_size+1):
        chop = text[i:i+pattern_size]
        if chop == pattern:
            count = count + 1
    return count


# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
def count_dict(text, k):
    count = {}
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i + k]
        count[i] = pattern_count(pattern, text)
    return count


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(' '.join(frequent_words(lines[0],int(lines[1]))))