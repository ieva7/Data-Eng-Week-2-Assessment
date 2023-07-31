"""Methods for test_1.py
Be advised that this code is adapted for Python v3.10 and later versions"""
from datetime import datetime


def is_log_line(line: str) -> bool | None:
    """Takes a log line and returns True if it is a valid log line and returns nothing
    if it is not.
    """
    try:
        segments = line.split(" ")
        date = segments.pop(0) + " " + segments.pop(0)
        date = datetime.strptime(date, "%m/%d/%y %H:%M:%S")

# Checking for 'valid' log levels from TODO: step 2 in is_log_line() to preserve modularity
        if isinstance(segments[0], str) and segments.pop(0) in \
                ["INFO", "TRACE", "WARNING"]:
            segments = " ".join(segments).strip()
            if segments[0] == ":":
                return True
    except Exception:  # catching broad exceptions due to instruction to return None if invalid line
        return None
    return None


def get_dict(line: str) -> dict | None:
    """Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
    try:
        if is_log_line(line):
            segments = line.split(" ")
            timestamp = segments.pop(0) + " " + segments.pop(0)
            log_level = segments.pop(0)

            return {"timestamp": timestamp, "log_level": log_level, "message":
                    " ".join(segments).strip()}
    except Exception:  # same as above, as well as to comply with the pre-written tests in test_1.py
        return None
    return None
