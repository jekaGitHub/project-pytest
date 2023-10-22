from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], 0, "None") == 1
    assert arrs.get([1, 2, 3, 4, 5, 6, 7], 7, "Not Found") == "Not Found"
    assert arrs.get([1, 2, 3], -1, "Negative number") == "Negative number"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 0, 1) == [1]
    assert arrs.my_slice([1, 2, 3], end=2) == [1, 2]
    assert arrs.my_slice([1, 2, 3, 4, 5, 6], -5, -2) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5, 6], -6, 6) == [1, 2, 3, 4, 5, 6]
