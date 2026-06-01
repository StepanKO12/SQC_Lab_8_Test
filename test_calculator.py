from calculator import add, multiply

def test_addition():
    assert add(2, 3) == 5

def test_multiplication():
    assert multiply(3, 4) == 12