import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """
    Repeat string s, n times, separated by spaces.

    :param s: String to be repeated.
    :param n: Number of times to repeat the string.
    :return: A new string with s repeated n times, separated by spaces.
    """
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Check if a word is at least a certain length.

    :param word: The word to check.
    :param length: Minimum length to be considered long. Defaults to 5.
    :return: True if word is equal to or longer than the specified length.
    """
    return len(word) >= length

def run_tests():
    """
    Run various assert tests to verify the functionality of functions.

    Tests the `repeat_string` function with two scenarios and the `Car` class for correct initialization of
    odometer and fuel attributes.
    """
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    # Check if the odometer is correctly set to 0 on initialization
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Test if the default fuel level is set correctly
    test_car_default_fuel = Car()
    assert test_car_default_fuel.fuel == 0, "Car default fuel is not set correctly."

    # Test if a custom fuel level is set correctly
    test_car_custom_fuel = Car(fuel=10)
    assert test_car_custom_fuel.fuel == 10, "Car custom fuel is not set correctly."

def format_sentence(phrase):
    """
    Format a given phrase as a complete sentence.

    This function capitalizes the first letter of the phrase and ensures it ends with a full stop.

    :param phrase: The phrase to format.
    :return: The formatted sentence.
    """
    sentence = phrase.capitalize()
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence

# Execute the test functions
run_tests()

# Run doctest to validate the function against specified test cases
doctest.testmod()
