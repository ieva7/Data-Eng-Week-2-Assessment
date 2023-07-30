# pylint: skip-file
import pytest

@pytest.fixture
def mock_court():
    """Returns fake court data as a dict"""
    return '[{"name": "Earls Court", "dx_number": "113 Liars Lane", "distance": "1"}]'