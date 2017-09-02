import pytest

from sec13exercisestep9.helpers import frequent_words


@pytest.mark.parametrize('n, input, output', ((4, 'ACGTTGCATGTCGCATGATGCATGAGAGCT', ['GCAT', 'CATG', 'GCAT', 'CATG', 'GCAT', 'CATG']),
                                              (5, 'CCGAACACCCGTACACCGAACACCACACCACACCTTGCACACCACACCTACACCACACACCACACCGGACACCCACACCCACACCACGAACACCGAGAGTACACCTA', ['ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC', 'ACACC'])))
def test_frequent_words(n, input, output):
    assert frequent_words(input, n) == output


