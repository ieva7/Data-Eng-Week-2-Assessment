"""Main file.
Reads .csv input and returns information about closest desired courts, as well
as people's data.
Output is produced to console.
"""
from rich.console import Console
from methods_test_2 import read_csv, get_court_by_postcode, filter_courts_by_desired_type,\
find_closest_court, add_court_information_to_person, render_table


PEOPLE_DATA_CSV_PATH = "./people.csv"

if __name__ == "__main__":
    try:
        people_data = read_csv(PEOPLE_DATA_CSV_PATH)
        console = Console(record=True)

        for person in people_data:
            courts = get_court_by_postcode(person["home_postcode"])
            courts_of_desired_type = filter_courts_by_desired_type(courts, \
                                            person["looking_for_court_type"])
            closest_court = find_closest_court(courts_of_desired_type)

            add_court_information_to_person(person, closest_court)

        render_table(people_data, console)

    # catching generalised exceptions to account for varied error raising in methods
    except Exception as e:
        print(e)
