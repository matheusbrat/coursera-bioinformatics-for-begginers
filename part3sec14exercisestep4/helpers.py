def pr(text, pro):
    prob = 1
    for i in range(len(text)):
        prob = float(prob) * float(pro[text[i]][i])
    return prob