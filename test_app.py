# Convention	        Meaning
# test_*.py	            Files starting with test_
# *_test.py	            Files ending with _test.py
# test_*()	            Functions starting with test_
# Test*	                Test classes starting with Test

from app import calculate_total


def test_calculate_total():
    assert calculate_total(100, 2) == 200


def test_zero_quantity():
    assert calculate_total(100, 0) == 0
