import pytest

from part3sec13exercisestep6.helpers import count

@pytest.mark.parametrize('i,o', ((['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG'], {'A': [1, 2, 1, 0, 0, 2], 'C': [2, 1, 4, 2, 0, 0], 'G': [1, 1, 0, 2, 1, 1], 'T': [1, 1, 0, 1, 4, 2]}),
                                 (['GTACAACTGT','CAACTATGAA','TCCTACAGGA','AAGCAAGGGT','GCGTACGACC','TCGTCAGCGT','AACAAGGTCA','CTCAGGCGTC','GGATCCAGGT','GGCAAGTACC'], {'A': [2, 3, 3, 3, 6, 4, 2, 2, 1, 3], 'C': [2, 3, 4, 3, 2, 3, 2, 1, 3, 3], 'G': [4, 2, 3, 0, 1, 3, 4, 5, 5, 0], 'T': [2, 2, 0, 4, 1, 0, 2, 2, 1, 4]})))
def test_count(i, o):
    assert count(i) == o
