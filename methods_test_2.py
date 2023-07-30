"""Method file for test_2.py"""
import csv
import requests
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table


def read_csv(file_path: str) -> list[dict]:
    """Reads a .csv file and returns a list[dict] excluding the header"""

    lines = []
    try:
        with open(file_path, "r") as csv_file:
            file_reader = csv.reader(csv_file, delimiter="\n")
            next(file_reader)
            for row in file_reader:
                row = row[0].split(",")
                lines.append({"person_name": row[0], "home_postcode": row[1], "looking_for_court_type"\
                        : row[2]})
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    except StopIteration:
        raise StopIteration("File is empty.")
    return lines


def get_court_by_postcode(home_postcode: str) -> list[dict] | None:
    """Searches the API by person's postcode and returns a list of all
    closest courts"""

    if not isinstance(home_postcode, str):
        raise TypeError("Postcode is not valid format.")

    courts = requests.get(f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode={home_postcode}")
    if courts.status_code == 200:
        return courts.json()
    elif courts.status_code == 400:
        print(f"Invalid postcode: {home_postcode}. Please try again.")

    return None


def filter_courts_by_desired_type(courts: list[dict], desired_court: str) -> list[dict] | None:
    """Searches given list of courts for those matching desired court type"""

    if not isinstance(courts, list):
        raise TypeError("Invalid type of courts provided.")

    if not isinstance(desired_court, str):
        raise TypeError("Invalid type of desired court provided.")

    matching_courts_found = []

    for court in courts:
        if desired_court in court["types"]:
            matching_courts_found.append(court)

    return matching_courts_found


# Can be easily amended to return multiple closest courts
def find_closest_court(courts: list[dict]) -> dict:
    """Searches given court list for the closest court.
    If two courts have the same closest distance, the former closest court is kept."""

    if not isinstance(courts, list):
        raise TypeError("Invalid type of courts provided.")

    if len(courts) < 1:
        raise ValueError("Courts list is empty.")

    closest_court = courts[0]
    for court in courts:
        if court["distance"] < closest_court["distance"]:
            closest_court = court

    return closest_court


# Can be easily amended to add a list of matching courts
# TEST
def add_court_information_to_person(person: dict, court: dict) -> None:
    """Adds matching court information to the person's dictionary"""
    if not isinstance(court, dict):
        raise TypeError("Invalid type of court provided.")

    if not isinstance(person, dict):
        raise TypeError("Invalid type of person data provided.")

    try:
        person["nearest_court"] = court["name"]
        person["distance_to_court"] = str(court["distance"])

        dx_number = court["dx_number"]
        if dx_number == None:
            dx_number = "Please refer to website"
        person["dx_number"] = dx_number
    except KeyError:
        raise KeyError("Missing information from courts.")
    except Exception as e:
        raise Exception(e)

#TEST
# Can be easily amended to display an individual's table of closest multiple courts
def render_table(people: list[dict]) -> Table:
    """Returns a rich.Table table with person's name, type of court desired, home postcode, nearest
    court of the right type, dx_number, and the distance to the nearest court as headers only."""

    information_table = Table(title="Information about the nearest courts")
    information_table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    information_table.add_column("Home postcode", style="magenta")
    information_table.add_column("Desired type of court", justify="right", style="slate_blue3")
    information_table.add_column("Nearest court", justify="right", style="green")
    information_table.add_column("Dx number", justify="right", style="yellow")
    information_table.add_column("Distance to court", justify="right", style="deep_pink2")

    for person in people:
        print("adding")
        information_table.add_row(person["person_name"], person["home_postcode"], person["looking_for_court_type"],\
        person["nearest_court"], person["dx_number"], person["distance_to_court"])

    console = Console(record=True)
    console.print(information_table)
