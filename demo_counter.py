"""Demo counter"""
from hpdl import Display
from micropython import const  # type: ignore
from time import sleep

counter = 0.0

data_pins = [0, 1, 2, 3, 4, 5, 6]  # D0 - D6
digit_pins = [40, 41]  # A0 - A1
write_pin = 42
display = Display(data_pins, digit_pins, write_pin)

try:
    while True:
        display.write_text(f"{counter:04.1f}")
        counter = round(counter + 0.1, 1) if counter < 99.9 else 0.0
        sleep(0.1)
except KeyboardInterrupt:
    print("\nCtrl-C pressed to exit.")
finally:
    display.clear()


