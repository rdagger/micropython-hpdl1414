"""HPDL-1414 Four Character Smart Alphanumeric Display Driver.

Pinout:
    1 = Data 5
    2 = Data 4
    3 = Write
    4 = Address 1
    5 = Address 0
    6 = 3.3V
    7 = Ground
    8 = Data 0
    9 = Data 1
    10 = Data 2
    11 = Data 3
    12 = Data 6
"""
from machine import Pin  # type: ignore
from time import sleep_us  # type: ignore


class Display(object):
    """HPDL Display Driver."""

    def __init__(self, data_pins, digit_pins, write_pin, digits=4):
        """Constructor for display driver.

        Args:
            data_pins([Pin]): List of data pins
            digit_pins([Pin]): List of digit pins
            write_pin(Pin): Write pin
            digits(int): Number of digits
        """
        self.data_pins = [Pin(p, Pin.OUT) for p in data_pins]
        self.digit_pins = [Pin(p, Pin.OUT) for p in digit_pins]
        self.write_pin = Pin(write_pin, Pin.OUT)
        self.write_pin.value(1)  # Write pin normally high
        self.digits = digits

    def clear(self):
        """Clear the display."""
        for digit in range(self.digits):
            self._write_raw("0000000", digit)

    def write_digit(self, character, digit):
        """Writes a character to the specified zero-based digit.

        Args:
            character(string): The character to write
            digit(int): The digit place to write (0-3 left to right)
        """
        # Ensure digit is valid
        assert (0 <= digit <= self.digits
                ), f"Error: digit {digit} > # of digits {self.digits}"
        ordinal = ord(character)
        # Ensure character in A-Z, 0-9, and  !"#$%&'<>*+,-./:;<=>?[/]^_
        assert (ordinal in range(ord(" "), ord("_") + 1)
                ), f"Error: character: {character} not in character set."
        data = f"{ordinal:07b}"  # Convert to 7 digit byte string
        self._write_raw(data, digit)

    def _write_raw(self, data, digit):
        """Write raw data to display.

        Args:
            data(str): The byte string to write
            digit(int): The digit place to write (0-3 left to right)
        """
        # Set data pins in LSB order
        for index, pin in enumerate(self.data_pins):
            pin.value(int(data[(len(self.data_pins) - 1) - index]))

        # Set digit address pin (reverse order to 0-3 instead of 3-0)
        for index, pin in enumerate(self.digit_pins):
            pin.value((((self.digits - 1) - digit) >> index) & 1)

        # Toggle write pin
        self.write_pin(0)
        sleep_us(1)
        self.write_pin(1)
        sleep_us(1)

    def write_text(self, text, position=0):
        """Write text to the display.

        Args:
            text(string): Text to write to display
            position(int): Starting digit 0-3 (left to right)
        """
        # Ensure text will fit
        assert (position + len(text) <= self.digits
                ), f"Text too long to fit at position {position}."
        for index, char in enumerate(text):
            self.write_digit(char, index + position)
