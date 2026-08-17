

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()


keyboard.col_pins = (board.D0, board.D1, board.D2)   
keyboard.row_pins = (board.D7, board.D8, board.D9)   
keyboard.diode_orientation = DiodeOrientation.COL2ROW  # TODO: prüfen (Diodenrichtung im Schaltplan, Pfeil zeigt zur Spalte)


keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6,
        KC.N1, KC.N2, KC.N3,
    ]
]


display_ext = Display(
    entries=[
        TextEntry(text="Hackpad", x=0, y=0),
        TextEntry(text="9 Tasten", x=0, y=12),
    ],
    width=128,
    height=32,
    driver=SSD1306(
        sda=board.SDA,
        scl=board.SCL,
        device_address=0x3C,  
    ),
)
keyboard.extensions.append(display_ext)

if __name__ == '__main__':
    keyboard.go()
