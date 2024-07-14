"""Demo text"""
from hpdl import Display
from time import sleep

data_pins = [0, 1, 2, 3, 4, 5, 6]  # D0 - D6
digit_pins = [40, 41]  # A0 - A1
write_pin = 42
display = Display(data_pins, digit_pins, write_pin)

display.write_text("ABCD")
sleep(3)

display.write_text("$@?_")
sleep(3)

display.write_text("0123")
sleep(2)

display.clear()
display.write_text("123", 1)
sleep(1)

display.clear()
display.write_text("23", 2)
sleep(1)

display.clear()
display.write_text("3", 3)
sleep(1)

display.clear()
