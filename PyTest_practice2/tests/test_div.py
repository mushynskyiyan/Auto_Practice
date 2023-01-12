from PyTest_practice2.some_code import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 5, 2),
                                                   (10, 2, 5),
                                                   (20, 10, 2)])
def test_div_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, number, devider", [(ZeroDivisionError, 10, 0),
                                                                 (TypeError, 10, "9"),
                                                                 (TypeError, "8", 2)])
def test_div_error(expected_exception, number, devider):
    with pytest.raises(expected_exception):
        division(number, devider)
