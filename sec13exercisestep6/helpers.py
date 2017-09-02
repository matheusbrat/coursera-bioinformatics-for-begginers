from sec12exercisestep15.helpers import pattern_count


def count_dict(text, k):
    count = {}
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i + k]
        count[i] = pattern_count(pattern, text)
    return count