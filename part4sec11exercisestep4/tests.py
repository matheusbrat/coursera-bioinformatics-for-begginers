import pytest

from part4sec11exercisestep4.helpers import count_with_pseudo

@pytest.mark.parametrize('i, o', ((['AACGTA','CCCGTT','CACCTT','GGATTA','TTCCGG'], {'A': [2, 3, 2, 1, 1, 3], 'C': [3, 2, 5, 3, 1, 1], 'T': [2, 2, 1, 2, 5, 3], 'G': [2, 2, 1, 3, 2, 2]}),
                                  (['GTACAACTGT','CAACTATGAA','TCCTACAGGA','AAGCAAGGGT','GCGTACGACC','TCGTCAGCGT','AACAAGGTCA','CTCAGGCGTC','GGATCCAGGT','GGCAAGTACC'], {'A': [3, 4, 4, 4, 7, 5, 3, 3, 2, 4], 'C': [3, 4, 5, 4, 3, 4, 3, 2, 4, 4], 'T': [3, 3, 1, 5, 2, 1, 3, 3, 2, 5], 'G': [5, 3, 4, 1, 2, 4, 5, 6, 6, 1]})))
def test_count_with_pesudo(i, o):
    assert count_with_pseudo(i) == o
