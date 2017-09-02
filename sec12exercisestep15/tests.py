import pytest
from sec12exercisestep15.helpers import pattern_count


@pytest.mark.parametrize('text,pattern,output', (('GCGCG', 'GCG', 2),
                                                 ('ACGTACGTACGT', 'CG', 3),
                                                 ('AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT', 'AAA', 4),
                                                 ('AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT', 'TTT', 4),
                                                 ('GGACTTACTGACGTACG', 'ACT', 2),
                                                 ('ATCCGATCCCATGCCCATG', 'CC', 5),
                                                 ('CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCTCTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACTCGCGCAGGTTGAGTA', 'CTC', 9)))
def test_pattern_count(text, pattern, output):
    assert pattern_count(pattern, text) == output
