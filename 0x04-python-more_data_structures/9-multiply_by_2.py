from roman import fromRoman

def roman_to_int(roman_string):
  """
  Converts a Roman numeral string to an integer using the roman library.

  Args:
      roman_string (str): The Roman numeral string.

  Returns:
      int: The integer equivalent of the Roman numeral.
  """

  try:
    return fromRoman(roman_string)
  except ValueError:  # Handle invalid Roman numeral input
    print(f"Invalid Roman numeral: {roman_string}")
    return None
