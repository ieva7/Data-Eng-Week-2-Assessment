"""Test file for methods_test_2.py"""
from io import StringIO
import json
import pytest
import requests_mock
from rich.console import Console
from methods_test_2 import read_csv, get_court_by_postcode, filter_courts_by_desired_type, \
find_closest_court, add_court_information_to_person, render_table



FAKE_URL = "https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E148HU"

# Testing: read_csv()

def test_read_csv_empty_file():
    """Empty file as input raises StopIteration"""
    with pytest.raises(StopIteration) as error:
        read_csv("./testing_materials/test_empty.csv")

    assert error.value.args[0] == "File is empty."


def test_read_csv_no_file():
    """File not found as input raises FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        read_csv("./testing_materials/453780542087425780457.csv")


def test_read_csv_valid_input(mock_person):
    """Valid input produces expected outcome of dict"""
    assert read_csv("./testing_materials/test_header_skip.csv")[0] == mock_person


# Testing: get_court_by_postcode

def test_get_court_invalid_postcode_type():
    """A non-string raises TypeError"""
    with pytest.raises(TypeError) as error:
        get_court_by_postcode(3322)

    assert error.value.args[0] == "Postcode is not valid format."


def test_get_court_postcode_not_found(postcode_not_found, capsys):
    """Postcode not being found prints a statement for developer."""
    with requests_mock.Mocker() as mock_url:
        mock_url.get(FAKE_URL + "3", text = postcode_not_found, status_code=400)
        message = get_court_by_postcode("E148HU3")

    captured = capsys.readouterr()

    assert message is None
    assert captured.out == "Invalid postcode: E148HU3. Please try again.\n"


def test_get_court_valid_input(mock_court):
    """Valid input returns a dictionary object with expected properties"""
    with requests_mock.Mocker() as mock_url:
        mock_url.get(FAKE_URL, text = mock_court)
        message = get_court_by_postcode("E148HU")

    assert isinstance(message, list)
    assert len(message) == 4
    assert isinstance(message[0], dict)
    assert message[0]["name"] == "Earls Court"


# Testing: filter_courts_by_desired_type()

def test_filter_courts_by_desired_type_invalid_courts_type():
    """A non-list of courts raises TypeError"""
    with pytest.raises(TypeError) as error:
        filter_courts_by_desired_type(3222222, "Family")

    assert error.value.args[0] == "Invalid type of courts provided."


def test_filter_courts_by_desired_type_invalid_desired_court_type():
    """A non-string of desired_court raises TypeError"""
    with pytest.raises(TypeError) as error:
        filter_courts_by_desired_type([{"name": "Earls Court"}], 3455555)

    assert error.value.args[0] == "Invalid type of desired court provided."


def test_filter_courts_by_desired_type_valid_input_types_found(mock_court):
    """Valid input returns a list of courts of desired types (case: found)"""
    courts = filter_courts_by_desired_type(json.loads(mock_court), "Family Court")

    assert len(courts) == 2
    assert courts[0]["types"] == ["Family Court"]


def test_filter_courts_by_desired_type_valid_input_types_not_found(mock_court):
    """Valid input returns a list of courts of desired types (case: not found)"""
    courts = filter_courts_by_desired_type(json.loads(mock_court), "Municipal Court")

    assert len(courts) == 0


# Testing: find_closest_court()

def test_find_closest_court_invalid_courts_type():
    """A non-list of courts raises TypeError"""
    with pytest.raises(TypeError) as error:
        find_closest_court(3222222)

    assert error.value.args[0] == "Invalid type of courts provided."


def test_find_closest_court_empty_courts():
    """A non-list of courts raises ValueError"""
    with pytest.raises(ValueError) as error:
        find_closest_court([])

    assert error.value.args[0] == "Courts list is empty."


def test_find_closest_court_valid_input(mock_court):
    """Valid input produces expected outcome."""

    court = find_closest_court(json.loads(mock_court))

    assert isinstance(court, dict)
    assert court["name"] == "Earls Court"



# Testing: add_court_information_to_person()

def test_add_court_information_to_person_invalid_person_type():
    """A non-dict of person input raises TypeError"""
    with pytest.raises(TypeError) as error:
        add_court_information_to_person(3222222, {"name": "Earls court"})

    assert error.value.args[0] == "Invalid type of person data provided."


def test_add_court_information_to_person_invalid_court_type():
    """A non-dict of court input raises TypeError"""
    with pytest.raises(TypeError) as error:
        add_court_information_to_person({"name": "Earl"}, 3496758945)

    assert error.value.args[0] == "Invalid type of court provided."


def test_add_court_information_to_person_invalid_court_information(mock_person):
    """Missing field from court with produce KeyError"""

    with pytest.raises(KeyError) as error:
        add_court_information_to_person(mock_person, {"name": "Earls court"})

    assert error.value.args[0] == "Missing information from courts."


def test_add_court_information_to_person_vaild_input(mock_court, mock_person):
    """Valid input yields expected results"""

    desired_court = json.loads(mock_court)[2]
    add_court_information_to_person(mock_person, desired_court)

    assert len(mock_person.keys()) == 6
    assert mock_person["dx_number"] == "135 Liars Lane"


# Testing: render_table()

def test_render_table_invalid_people_type():
    """A non-list of people input raises TypeError"""

    console = Console()
    with pytest.raises(TypeError) as error:
        render_table(3496758945, console)

    assert error.value.args[0] == "Invalid type of people data provided."


def test_render_table_missing_keys(mock_person):
    """Errors in adding table rows will raise KeyError"""

    console = Console()
    with pytest.raises(KeyError) as error:
        render_table([mock_person], console)

    assert error.value.args[0] == "Key invalid. Please check your data source."


def test_render_table_invalid_console_type(mock_person):
    """Invalid type of console input will raise TypeError"""

    with pytest.raises(TypeError) as error:
        render_table([mock_person], 13243123)

    assert error.value.args[0] == "Invalid type of console provided."


def test_render_table_valid_input(mock_person, mock_court):
    """Valid input will produce a successful table with expected information"""

    desired_court = json.loads(mock_court)[2]
    add_court_information_to_person(mock_person, desired_court)


    console = Console(file=StringIO(), record=True)
    render_table([mock_person], console)
    output = console.file.getvalue()

    assert "Information about the nearest courts" in output
    assert "Iriquois Pliskin" in output
