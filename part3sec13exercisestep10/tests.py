import pytest

from part3sec13exercisestep10.helpers import consensus

@pytest.mark.parametrize('i,o', ((['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG'], 'CACCTA'),
                                 (['GTACAACTGT','CAACTATGAA','TCCTACAGGA','AAGCAAGGGT','GCGTACGACC','TCGTCAGCGT','AACAAGGTCA','CTCAGGCGTC','GGATCCAGGT','GGCAAGTACC'], 'GACTAAGGGT')))
def test_consensus(i, o):
    assert consensus(i) == o
