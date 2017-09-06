import pytest

from part2sec14exercisestep3.helpers import skew as skew_func


@pytest.mark.parametrize('inp, output', (('CATGGGCATCGGCCATACGCC', '0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2'),
                                         ('AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT', '0 0 1 0 1 1 2 1 0 1 1 1 1 1 1 1 2 1 0 1 0 -1 -1 0 0 -1 -2 -2 -1 -2 -2 -1 -2 -1 0 0 1 2 1 0 0 -1 0 -1 -2 -1 -1 -2 -2 -2 -3 -3 -4 -3 -2 -2 -2 -1 -2 -3 -3 -3 -2 -2 -1 -2 -2 -2 -2 -1 -1 0 1 1 1 2 1 2 2 3 2 2 2 2 3 4 4 5 6 6 6 6 5 5 5 5 4 5 4 4 4 4 4 4 3 2 2 3 2 3 2 3 3 3 3 3 2 1 1 0 1 1 1 0 0 1 1 2 1 0 1 1 0 0 0 0')))
def test_skew(inp, output):
    skew = skew_func(inp)
    assert ' '.join([str(skew[i]) for i in sorted(skew.keys())]) == output
