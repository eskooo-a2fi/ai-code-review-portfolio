import pytest
from corrected_fibonacci import fibonacci


def test_known_values():
    assert [fibonacci(i) for i in range(11)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_large_index():
    assert fibonacci(100) == 354224848179261915075


@pytest.mark.parametrize('value', [-1, -10])
def test_negative_rejected(value):
    with pytest.raises(ValueError):
        fibonacci(value)


@pytest.mark.parametrize('value', [True, 3.5, '5', None])
def test_invalid_type_rejected(value):
    with pytest.raises(TypeError):
        fibonacci(value)
