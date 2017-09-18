import pytest

from part3sec14exercisestep5.helpers import pmpp

x = """0.2 0.2 0.3 0.2 0.3
    0.4 0.3 0.1 0.5 0.1
    0.3 0.3 0.5 0.2 0.4
    0.1 0.2 0.1 0.1 0.2"""

y = """0.7 0.2 0.1 0.5 0.4 0.3 0.2 0.1
    0.2 0.2 0.5 0.4 0.2 0.3 0.1 0.6
    0.1 0.3 0.2 0.1 0.2 0.1 0.4 0.2
    0.0 0.3 0.2 0.0 0.2 0.3 0.3 0.1"""

z = """0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.1 0.2 0.3 0.4 0.5
    0.3 0.2 0.1 0.1 0.2 0.1 0.1 0.4 0.3 0.2 0.2 0.1
    0.2 0.1 0.4 0.3 0.1 0.1 0.1 0.3 0.1 0.1 0.2 0.1
    0.3 0.4 0.1 0.1 0.1 0.1 0.0 0.2 0.4 0.4 0.2 0.3"""

t = """1.0 1.0 1.0
    0.0 0.0 0.0
    0.0 0.0 0.0
    0.0 0.0 0.0"""

k = """0.2 0.2 0.3 0.2 0.3
    0.4 0.3 0.1 0.5 0.1
    0.3 0.3 0.5 0.2 0.4
    0.1 0.2 0.1 0.1 0.2"""


@pytest.mark.parametrize('text, size, profile, o', (('ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT', 5, x, 'CCGAG'),
                                        ('AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAACTGGTTACCTGCCGTGAGTAAAT', 8, y, 'AGCAGCTT'),
                                        ('TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA', 12, z, 'AAGCAGAGTTTA'),
                                        ('AACCGGTT', 3, t, 'AAC'),
                                        ('TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA', 5, k, 'CAGCG')))
def test_pr(text, size, profile, o):
    profile = profile.strip()
    l = []
    for line in profile.split('\n'):
        l.append(line.strip().split(' '))
    profile = {'A': l[0], 'C': l[1], 'G': l[2], 'T': l[3]}
    assert pmpp(text, size, profile) == o
