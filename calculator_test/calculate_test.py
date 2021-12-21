from calculator.calculate import add, subtract, multiply, divide

def test_add():
    assert add(3, 1) == 4
    assert add(70, -14) == 56

def test_subtract():
    assert subtract(3, 1) == 2
    assert subtract(70, -14) == 84

def test_multiply():
    assert multiply(3, 1) == 3
    assert multiply(70, -14) == -980

def test_divide():
    assert divide(3, 1) == 3
    assert divide(70, -14) == -5


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()

