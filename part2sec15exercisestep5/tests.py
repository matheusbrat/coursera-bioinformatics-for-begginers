import pytest

from part2sec15exercisestep5.helpers import approximate_pattern_count

@pytest.mark.parametrize('p, t, d, o', (('GAGG', 'TTTAGAGCCTTCAGAGG', 2, 4),
                                        ('AA', 'AAA', 0, 2),
                                        ('ATA', 'ATA', 1, 1),
                                        ('GTGCCG', 'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT', 3, 24)))
def test_approximate_pattern_count(p,t,d,o):
    assert approximate_pattern_count(p,t,d) == o
