import sys
from enum import Enum


class YesOrNo(Enum):
    YES = 1
    NO = 0


class EmptyInputError(ValueError):
    """Custom exception for empty input."""
    pass


class OutOfRangeError(ValueError):
    """Custom exception for values outside the allowed range."""

    def __init__(self, value, min_value, max_value):
        super().__init__(f"Input {value} is out of range ({min_value} to {max_value}).")
        self.value = value
        self.min_value = min_value
        self.max_value = max_value


class StringLengthError(ValueError):
    """Custom exception for strings that are too short or too long."""

    def __init__(self, value, min_length, max_length):
        super().__init__(f"Input '{value}' must be between {min_length} and {max_length} characters long.")
        self.value = value
        self.min_length = min_length
        self.max_length = max_length


def input_valid_string(prompt: str, min_length: int = 0, max_length: int = sys.maxsize) -> str:
    """Function to get a valid string input, enforcing length constraints."""
    user_input = input(prompt).strip()  # Entfernt führende und nachfolgende Leerzeichen

    if not (min_length <= len(user_input) <= max_length):
        raise StringLengthError(user_input, min_length, max_length)

    return user_input  # Gültige Zeichenkette zurückgeben


def input_valid_int(prompt: str, min_value: int = -sys.maxsize, max_value: int = sys.maxsize,
                    default: int = None) -> int:

    user_input = input(prompt).strip()
    if user_input == "":
        if default is None:
            raise EmptyInputError("Input cannot be empty.")
        else:
            return default

    try:
        value = int(user_input)  # Versuch, die Eingabe in eine Zahl umzuwandeln
    except ValueError as err:
        raise ValueError("Invalid input. Please enter a valid number.") from err  # Exception-Chaining

    if value < min_value or value > max_value:
        raise OutOfRangeError(value, min_value, max_value)  # Eigene Exception für Werte außerhalb des Bereichs

    return value  # Gültige Zahl zurückgeben


def input_valid_float(
        prompt: str,
        min_value: float = -float('inf'),
        max_value: float = float('inf'),
        default: float = None
) -> float:
    """Function to get a valid float within a range, raising specific exceptions."""
    user_input = input(prompt).strip()

    if user_input == "":
        if default is None:
            raise EmptyInputError("Input cannot be empty.")
        else:
            return default

    try:
        value = float(user_input)  # Versuch, die Eingabe in eine Fließkommazahl umzuwandeln
    except ValueError as err:
        raise ValueError("Invalid input. Please enter a valid float number.") from err  # Exception-Chaining

    if value < min_value or value > max_value:
        raise OutOfRangeError(value, min_value, max_value)  # Eigene Exception für Werte außerhalb des Bereichs

    return value  # Gültige Zahl zurückgeben


def input_y_n(prompt: str, default: YesOrNo = None) -> bool:
    y = ['y', 'yes']
    n = ['n', 'no']

    user_input = input(prompt).strip().lower()
    match user_input:
        case _ if user_input in y:
            return True
        case _ if user_input in n:
            return False
        case _:
            if user_input == "" and default:
                return bool(default.value)
            else:
                raise ValueError(f"Invalid input. Please enter 'y' or 'n'.")
