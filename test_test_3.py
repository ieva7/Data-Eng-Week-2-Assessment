"""Test file for test_3.py"""

import pytest
from test_3 import sum_current_time



def test_sum_current_time_invalid_input_type():
    """Invalid input type will raise TypeError"""

    with pytest.raises(TypeError) as error:
        sum_current_time(34)

    assert error.value.args[0] == "Incorrect type of input provided, <class 'int'> not allowed."


def test_sum_current_time_invalid_string(capsys):
    """Invalid string format will print a ValueError message to console"""

    sum_current_time("3:3:3:3")

    captured = capsys.readouterr()
    assert captured.out == "String does not contain time-formatted data.\n"


def test_sum_current_time_invalid_string_2(capsys):
    """Invalid string format without ':' will produce ValueError"""

    sum_current_time("aa")

    captured = capsys.readouterr()
    assert captured.out == "String does not contain time-formatted data.\n"


def test_sum_current_time_invalid_string_3(capsys):
    """Invalid string with non-number values will produce ValueError"""

    sum_current_time("aa:aa:aa")

    captured = capsys.readouterr()
    assert "invalid literal" in captured.out


def test_sum_current_time_invalid_hour(capsys):
    """Invalid hour value will produce ValueError"""

    sum_current_time("25:11:11")

    captured = capsys.readouterr()
    assert captured.out == "Hour value over 23; please provide only time-format strings.\n"


def test_sum_current_time_invalid_minute(capsys):
    """Invalid minute value will produce ValueError"""

    sum_current_time("23:60:11")

    captured = capsys.readouterr()
    assert captured.out == "Minute/second value over 59; please provide only time-format strings.\n"


def test_sum_current_time_too_long_number(capsys):
    """Invalid minute value will produce ValueError"""

    sum_current_time("001:000:001")

    captured = capsys.readouterr()
    assert captured.out == "Number is not two digits; please provide only time-format strings.\n"


def test_sum_current_time_invalid_second(capsys):
    """Invalid minute value will produce ValueError"""

    sum_current_time("23:40:61")

    captured = capsys.readouterr()
    assert captured.out == "Minute/second value over 59; please provide only time-format strings.\n"


def test_sum_current_time_valid_input():
    """Valid input will produce a sum"""

    sum_num = sum_current_time("12:12:12")

    assert isinstance(sum_num, int)
    assert sum_num == 36


def test_sum_current_time_valid_input_zero():
    """Valid input will produce a sum"""

    sum_num = sum_current_time("00:00:00")

    assert isinstance(sum_num, int)
    assert sum_num == 0
