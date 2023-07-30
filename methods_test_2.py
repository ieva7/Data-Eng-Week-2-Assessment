"""Method file for test_2.py"""
import csv
import requests
import json


def read_csv(file_path: str) -> list[str]:
    """Reads a .csv file and returns a list[str] excluding the header"""

    lines = []
    try:
        with open(file_path, "r") as csv_file:
            file_reader = csv.reader(csv_file, delimiter="\n")
            next(file_reader)
            for row in file_reader:
                lines.append(row)
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    except StopIteration:
        raise StopIteration("File is empty.")
    return lines


def get_court_by_postcode(home_postcode: str) -> list[dict] | None:
    """Searches the API by person's postcode and returns a list of all
    closest courts"""

    if not isinstance(home_postcode, str):
        raise TypeError("Postcode Invalid")

    courts = requests.get(f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode={home_postcode}")
    if courts.status_code == 200:
        return courts.json()
    else:
        return None

get_court_by_postcode("E148HU")