from exercisestep6part2.helpers import count_dict


def frequent_words(text, k):
    frequent_patterns = []
    cdict = count_dict(text, k)
    m = max(cdict.values())
    for i in cdict:
        if cdict[i] == m:
            frequent_patterns.append(text[i:i + k])
    return frequent_patterns