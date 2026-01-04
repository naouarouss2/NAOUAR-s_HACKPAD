import board
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros, Tap
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

# =========================
# Keyboard instance
# =========================
keyboard = KMKKeyboard()

# =========================
# Matrix configuration
# =========================
keyboard.matrix = MatrixScanner(
    columns=[
        board.GP26,  # C0
        board.GP27,  # C1
        board.GP28,  # C2
        board.GP29,  # C3
    ],
    rows=[
        board.GP3,   # R0 (top)
        board.GP4,   # R1
        board.GP2,   # R2
        board.GP1,   # R3 (bottom)
    ],
    diode_orientation=MatrixScanner.DIODE_COL2ROW,
)

# =========================
# Layers
# =========================
layers = Layers()
keyboard.modules.append(layers)

# =========================
# Macros
# =========================
macros = Macros()
keyboard.modules.append(macros)

# Example macros
COPY = KC.MACRO(Tap(KC.LCTRL), Tap(KC.C))
PASTE = KC.MACRO(Tap(KC.LCTRL), Tap(KC.V))
UNDO = KC.MACRO(Tap(KC.LCTRL), Tap(KC.Z))
HELLO = KC.MACRO("Hello world!")

# =========================
# Encoder (matrix-wired)
# =========================
encoder = EncoderHandler()
encoder.pins = (
    ((1, 3), (2, 3))  # (B_row, A_row) → rows 3 & 2 on column 4
)
encoder.map = [
    (KC.VOLU, KC.VOLD),  # Layer 0
    (KC.RIGHT, KC.LEFT),# Layer 1
    (KC.BRIU, KC.BRID), # Layer 2
    (KC.PGDN, KC.PGUP), # Layer 3
]
keyboard.modules.append(encoder)

# =========================
# RGB (NeoPixel)
# =========================
rgb = RGB(
    pixel_pin=board.GP0,
    num_pixels=15,
    val_limit=100,
    hue_default=0,
    sat_default=255,
    val_default=80,
    animation_speed=3,
)
rgb.enable_rainbow()
keyboard.extensions.append(rgb)

# =========================
# OLED Display (128x32)
# =========================
display = Display(
    display=SSD1306(
        i2c=board.I2C(),
        device_address=0x3C,
        width=128,
        height=32,
    ),
    entries=[
        TextEntry(
            text="Layer:",
            x=0,
            y=0,
        ),
        TextEntry(
            text=lambda: str(keyboard.active_layers[0]),
            x=60,
            y=0,
        ),
    ],
)
keyboard.extensions.append(display)

# =========================
# Keymap (4 layers)
# 4 columns × 4 rows
# =========================
keyboard.keymap = [
    # ---------- Layer 0 ----------
    [
        KC.N1,    KC.N2,    KC.N3,    KC.TG(1),
        KC.Q,     KC.W,     KC.E,     KC.TG(2),
        KC.A,     KC.S,     KC.D,     KC.TG(3),
        COPY,     PASTE,    UNDO,     KC.NO,
    ],

    # ---------- Layer 1 ----------
    [
        KC.F1,    KC.F2,    KC.F3,    KC.TG(0),
        KC.LEFT,  KC.DOWN,  KC.UP,    KC.RIGHT,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,
        HELLO,    KC.NO,    KC.NO,    KC.NO,
    ],

    # ---------- Layer 2 ----------
    [
        KC.BRIU,  KC.BRID,  KC.NO,    KC.TG(0),
        KC.MPRV,  KC.MPLY,  KC.MNXT,  KC.NO,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,
    ],

    # ---------- Layer 3 ----------
    [
        KC.PGUP,  KC.PGDN,  KC.HOME,  KC.TG(0),
        KC.NO,    KC.NO,    KC.NO,    KC.NO,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,
        KC.RESET, KC.NO,    KC.NO,    KC.NO,
    ],
]

# =========================
# Go!
# =========================
if __name__ == "__main__":
    keyboard.go()
