import pytest

from part3sec13exercisestep11.helpers import score

@pytest.mark.parametrize('i,o', ((['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG'], 14),
                                 (['GTACAACTGT','CAACTATGAA','TCCTACAGGA','AAGCAAGGGT','GCGTACGACC','TCGTCAGCGT','AACAAGGTCA','CTCAGGCGTC','GGATCCAGGT','GGCAAGTACC'], 57)))
def test_score(i, o):
    assert score(i) == o
