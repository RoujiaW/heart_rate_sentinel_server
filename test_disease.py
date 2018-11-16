import pytest
from disease import disease


def test_disease():
    with pytest.raises(TypeError):
        disease(None, "1")
    with pytest.raises(TypeError):
        disease([1], "test")

    assert disease(2, 160) is True
    assert disease(6, 145) is True
    assert disease(40, 101) is True
    assert disease(56, 91) is False
    assert disease(10, 117) is False
