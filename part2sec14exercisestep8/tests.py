import pytest

from part2sec14exercisestep8.helpers import min_skew

@pytest.mark.parametrize('inp, output', (('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT', [11, 24]),
                                         ('ACCG', [3]),
                                         ('ACCC', [4]),
                                         ('CCGGGT', [2]),
                                         ('CCGGCCGG', [2, 6]),
                                         ('AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT', [52])))
def test_min_skew(inp, output):
    assert min_skew(inp) == output
