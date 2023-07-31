"""Main file for test_3. """


def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS.
    Converts given time to numbers and returns their sum"""

    if not isinstance(time_str, str):
        raise TypeError(f"Incorrect type of input provided, {type(time_str)} not allowed.")

    try:
        list_of_nums = time_str.split(":")
        if len(list_of_nums) != 3:
            raise ValueError("String does not contain time-formatted data.")

        for count, num in enumerate(list_of_nums):
            if len(num) > 2:
                raise ValueError("Number is not two digits; please provide only time-format strings.") # pylint: disable=line-too-long

            num = int(num)

            if count == 0:
                if num > 23:
                    raise ValueError("Hour value over 23; please provide only time-format strings.")
            if num < 0:
                raise ValueError("Time value is negative; please provide only time-formatted strings.") # pylint: disable=line-too-long
            if num > 59:
                raise ValueError("Minute/second value over 59; please provide only time-format strings.") # pylint: disable=line-too-long
            list_of_nums[count] = num

        return sum(list_of_nums)
    except ValueError as error:
        print(error)
    except Exception as exc: # general exception catcher for unforeseen errors
        print(exc)
