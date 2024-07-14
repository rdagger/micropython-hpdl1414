"""Demo character set"""
from hpdl import Display
from time import sleep

data_pins = [0, 1, 2, 3, 4, 5, 6]  # D0 - D6
digit_pins = [40, 41]  # A0 - A1
write_pin = 42
display = Display(data_pins, digit_pins, write_pin)

start = ord(" ")
end = ord("_")

for x in range(start, end + 1):
    display.clear()
    display.write_text(chr(x) * 4)
    print(x, chr(x))
    sleep(1)

display.clear()
