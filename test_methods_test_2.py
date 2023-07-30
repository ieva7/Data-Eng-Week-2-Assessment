# pylint: skip-file

from methods_test_2 import read_csv, get_court_by_postcode
import pytest
import requests_mock
import requests

FAKE_URL = "https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E148HU"

# Testing: read_csv()

def test_read_csv_empty_file():
    """Empty file as input"""
    with pytest.raises(StopIteration) as e:
        read_csv("./testing_materials/test_empty.csv")

    assert e.value.args[0] == "File is empty."


def test_read_csv_no_file():
    """File not found as input"""
    with pytest.raises(FileNotFoundError):
        read_csv("./testing_materials/453780542087425780457.csv")


def test_read_csv_valid_input_skips_header():
    """Checks that first line of file (header) is ignored"""
    assert read_csv("./testing_materials/test_header_skip.csv")[0] ==\
    ["Iriquois Pliskin,SE17TP,Crown Court"]


# Testing: get_court_by_postcode


def test_get_court_invalid_postcode():
    """A non-string raises TypeError"""
    with pytest.raises(TypeError):
        get_court_by_postcode(3322)


def test_get_court_valid_input(mock_court):
    """Valid input returns a dictionary object with expected properties"""
    with requests_mock.Mocker() as m:
        m.get(FAKE_URL, text = mock_court)
        message = get_court_by_postcode("E148HU")

    assert isinstance(message, list)
    assert isinstance(message[0], dict)
    assert message[0]["name"] == "Earls Court"