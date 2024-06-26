#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    total = 0
    i = 0
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    for char in roman_string:
        value = roman_to_int.get(char, 0)
        if value > i:
            total += value - i * 2
        else:
            total += value
        i = value
    return total
