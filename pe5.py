import pytest

multi_table = [['X' if i == j == 0 else max(i, j) if i == 0 or j == 0 else i*j for i in range(0, 13)]
               for j in range(0, 13)]

# i) 2 basic tests
@pytest.mark.basic
def test_basic_multiplication():
    assert multi_table[5][7] == 35
    assert multi_table[6][8] == 48

# ii) One test marked to expect failure
@pytest.mark.xfail
def test_fail_case():
    assert multi_table[2][5] == 100  # This test will fail intentionally

# iii) Test for IndexError
def test_index_error():
    with pytest.raises(IndexError):
        _ = multi_table[13][0]  # Accessing a row index exceeding 12
        _ = multi_table[0][13]  # Accessing a column index exceeding 12

# iv) Parametrized test with multiple input-output combinations
@pytest.mark.parametrize("i, j, expected", [(2, 3, 6), (4, 6, 24), (6, 9, 54), (12, 12, 144)])
def test_parametrized_multiplication(i, j, expected):
    assert multi_table[i][j] == expected
