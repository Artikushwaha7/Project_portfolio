'''

Regular Expressions
Functions
Error Handling
Conditionals

'''

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if " to " not in s:
        raise ValueError("Invalid time format: missing ' to '")

    pattern = r'^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\sto\s(\d{1,2})(?::(\d{2}))?\s(AM|PM)$'
    match = re.fullmatch(pattern, s.strip())
    if not match:
        raise ValueError("Invalid time format")

    hour1, minute1, period1, hour2, minute2, period2 = match.groups()

    time1 = convert_to_24_hour(hour1, minute1, period1)
    time2 = convert_to_24_hour(hour2, minute2, period2)

    return f"{time1} to {time2}"

def convert_to_24_hour(hour_str, minute_str, period):
    try:
        hour = int(hour_str)
        if minute_str is None:
            minute = 0
        else:
            minute = int(minute_str)
    except ValueError:
        raise ValueError("Invalid time")

    if not (1 <= hour <= 12):
        raise ValueError("Invalid hour")
    if not (0 <= minute <= 59):
        raise ValueError("Invalid minute")

    if period == 'AM':
        if hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
    else:
        if hour == 12:
            hour_24 = 12
        else:
            hour_24 = hour + 12

    return f"{hour_24:02d}:{minute:02d}"



if __name__ == "__main__":
    main()
