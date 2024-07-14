"""Demo digits"""
from hpdl import Display
from time import sleep

data_pins = [0, 1, 2, 3, 4, 5, 6]  # D0 - D6
digit_pins = [40, 41]  # A0 - A1
write_pin = 42
display = Display(data_pins, digit_pins, write_pin)

for i in range(4):
    display.clear()
    display.write_digit(str(i), i)
    print(f"Digit: {i}")
    sleep(1)

sleep(1)

for i in range(4):
    display.clear()
    display.write_digit(chr(i+65), i)
    print(f"Digit: {i}")
    sleep(1)

display.clear()
