from app import calculate_total


def test_calculate_total():
    assert calculate_total(100, 2) == 200


def test_zero_quantity():
    assert calculate_total(100, 0) == 0
