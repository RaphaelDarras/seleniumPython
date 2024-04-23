import pytest

def test_monPremierTest():
    assert 1 == 2




def test_cestQuandMes60():
    cestQuandMes60 = lambda age : 60 - age
    age = 20
    try:
        assert cestQuandMes60(age) == 20
        assert 1 == 2
    except AssertionError:
        print('Test failed')