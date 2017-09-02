import pytest

from sec14exercisestep7.helpers import pattern_matching


@pytest.mark.parametrize('pattern, genome, output', (('ATAT', 'GATATATGCATATACTT', [1, 3, 9]),
                                                     ('ACAC', 'TTTTACACTTTTTTGTGTAAAAA', [4]),
                                                     ('AAA', 'AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT', [0, 46, 51, 74]),
                                                     ('TTT', 'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT', [88, 92, 98, 132]),
                                                     ('ATA', 'ATATATA', [0, 2, 4])))
def test_pattern_matching(pattern, genome, output):
    assert pattern_matching(pattern, genome) == output

