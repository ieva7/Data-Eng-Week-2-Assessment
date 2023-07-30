# pylint: skip-file
from methods_test_1 import get_dict, is_log_line


# Testing: is_log_line()

def test_is_log_line_unsuccessful_outcome():
    assert is_log_line("03/11/21 08:51:01 INFO: locate_configFile: \
            Specified configuration \file: /u/user10/rsvpd1.conf") == None


def test_is_log_line_empty_line():
    assert is_log_line("\n") == None


def test_is_log_line_invalid_input():
    assert is_log_line(3579359785398753789) == None


def test_is_log_line_successful_outcome():
    assert is_log_line("03/11/21 08:51:01 INFO    :...locate_configFile: \
        Specified configuration file: /u/user10/rsvpd1.conf") == True


# Testing: get_dict()

def test_get_dict_unsuccessful_outcome():
    assert get_dict("03/11/21 08:51:01 INFO    ...locate_configFile: \
        Specified configuration file: /u/user10/rsvpd1.conf") == None


def test_get_dict_invalid_input():
    assert get_dict(5429752489742587932879) == None


def test_get_dict_successful_outcome():
    assert get_dict("03/11/21 08:51:01 INFO    :...locate_configFile: \
        Specified configuration file: /u/user10/rsvpd1.conf") == {"timestamp": \
        "03/11/21 08:51:01", "log_level": "INFO", "message": ":...locate_configFile: \
        Specified configuration file: /u/user10/rsvpd1.conf"}








