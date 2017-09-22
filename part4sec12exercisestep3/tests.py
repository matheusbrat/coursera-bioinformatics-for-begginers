import pytest

from part4sec12exercisestep3.helpers import motifs

m = {'A': [0.8, 0.0, 0.0, 0.2], 'C': [0.0, 0.6, 0.2, 0.0], 'G': [0.2, 0.2, 0.8, 0.0], 'T': [0.0, 0.2, 0.0, 0.8]}

dna = """TTACCTTAAC
GATGTCTGTC
ACGGCGTTAG
CCCTAACGAG
CGTCAGAGGT""".split('\n')

m1 = {'A': [0.5, 0.0, 0.2, 0.2], 'G': [0.2, 0.2, 0.6, 0.0], 'T': [0.0, 0.2, 0.0, 0.8], 'C': [0.3, 0.6, 0.2, 0.0]}


dna1 = """TTACCTTAAC
    GATGTCTGTC
    ACGGCGTTAG
    CCCTAACGAG
    CGTCAGAGGT""".split('\n')

@pytest.mark.parametrize('m, dna, o', ((m, dna, ['ACCT','ATGT','GCGT','ACGA','AGGT']),
                                       (m1, dna1, ['ACCT','ATGT','GCGT','ACGA','AGGT'])))
def test_motifs(m, dna, o):
    assert motifs(m, dna) == o
