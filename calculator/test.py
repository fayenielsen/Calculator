import calculate

def test_add():
    assert calculate.add(3, 1) == 4
    assert calculate.add(70, -14) == 56

def test_subtract():
    assert calculate.subtract(3, 1) == 2
    assert calculate.subtract(70, -14) == 84

def test_multiply():
    assert calculate.multiply(3, 1) == 3
    assert calculate.multiply(70, -14) == -980

def test_divide():
    assert calculate.divide(3, 1) == 3
    assert calculate.divide(70, -14) == -5


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()

