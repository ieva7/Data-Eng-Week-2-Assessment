"""Test file for methods_test_1.py"""
from methods_test_1 import get_dict, is_log_line


# Testing: is_log_line()

def test_is_log_line_no():
    """Invalid log line will return None"""
    assert is_log_line("03/11/21 08:51:01 INFO: locate_configFile: \
            Specified configuration \file: /u/user10/rsvpd1.conf") is None


def test_is_log_line_empty_line():
    """Empty line (newline) will return None"""
    assert is_log_line("\n") is None


def test_is_log_line_invalid_input():
    """Invalid input will return None"""
    assert is_log_line(3579359785398753789) is None


def test_is_log_line_successful_outcome():
    """Valid successful input will yield True"""
    assert is_log_line("03/11/21 08:51:01 INFO    :...locate_configFile: \
        Specified configuration file: /u/user10/rsvpd1.conf") is True


# Testing: get_dict()

def test_get_dict_unsuccessful_outcome():
    """Invalid log line will return None"""
    assert get_dict("03/11/21 08:51:01 INFO    ...locate_configFile: \
        Specified configuration file: /u/user10/rsvpd1.conf") is None


def test_get_dict_invalid_input():
    """Invalid type of input will return None"""
    assert get_dict(5429752489742587932879) is None


def test_get_dict_successful_outcome():
    """Valid successful input will yield a dictionary object"""
    assert get_dict("03/11/21 08:51:01 INFO    :...locate_configFile: \
        Specified configuration file: /u/user10/rsvpd1.conf") == {"timestamp": \
        "03/11/21 08:51:01", "log_level": "INFO", "message": ":...locate_configFile: \
        Specified configuration file: /u/user10/rsvpd1.conf"}
