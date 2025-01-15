import pytest
from prime_check import is_prime

def test_is_prime():
    assert is_prime(2) == True  # 2 is prime
    assert is_prime(3) == True  # 3 is prime
    assert is_prime(5) == True  # 5 is prime
    assert is_prime(7) == True  # 7 is prime

