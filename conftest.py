# pylint: skip-file
import pytest


@pytest.fixture
def mock_person():
    """Returns fake person data"""
    return {"person_name": "Iriquois Pliskin","home_postcode": "SE17TP","looking_for_court_type": "Crown Court"}


@pytest.fixture
def mock_court():
    """Returns fake court data"""
    return '''[{"name": "Earls Court", "types": ["Family Court"], "dx_number": "113 Liars Lane",
    "distance": "1"}, {"name": "Greys Court", "types": ["Family Court", "Tribunal"], "dx_number":
    "118 Liars Lane", "distance": "1"}, {"name": "Malfoys Court", "types": ["Tribunal"], "dx_number":
    "135 Liars Lane", "distance": "1.9"}, {"name": "Unfiled Court", "types": [], "dx_number":
    "200 Liars Lane", "distance": "2.5"}]'''


@pytest.fixture
def postcode_not_found():
    """Returns a message of postcode not being found"""
    return '{"message": "Invalid postcode: E148HU3"}'