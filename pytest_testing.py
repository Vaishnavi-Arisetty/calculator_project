import pytest
import Calculator as Ca


def test_add():
    assert Ca.add(10, 10) == 20


def test_sub():
    assert Ca.sub(10, 9) == 1


def test_multiply():
    assert Ca.multiply(2, 3) == 6


def test_divide():
    assert Ca.divide(2, 10) == 0.2
    with pytest.raises(ZeroDivisionError):
        Ca.divide(2, 0)


def test_square():
    assert Ca.square(5) == 25


def test_square_root():
    assert Ca.square_root(9) == 3
    with pytest.raises(ValueError):
        Ca.square_root(-9)


def test_sine():
    assert Ca.sine(90) == 1


def test_cosine():
    assert Ca.cosine(0) == 1


def test_tangent():
    assert pytest.approx(Ca.tangent(45)) == 1


def test_log():
    assert Ca.logarithm(100) == 2
    with pytest.raises(ValueError):
        Ca.logarithm(-10)


def test_reciprocal():
    assert Ca.reciprocal(10) == 0.1
    with pytest.raises(ZeroDivisionError):
        Ca.reciprocal(0)


test_add()
test_sub()
test_multiply()
test_divide()
test_square()
test_square_root()
test_sine()
test_cosine()
test_tangent()
test_log()
test_reciprocal()