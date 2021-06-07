"""
Test for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_sub(self):
        assert 5 == calculator.sub(10, 5)

    def test_mult(self):
        assert 10 == calculator.mult(2, 5)

    def test_div(self):
        assert 6 == calculator.div(3, 2)
