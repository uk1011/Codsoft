import math
#SIZE OF GUI
CALCULATOR_SIZE = (400,700)
ROWS = 7
COLUMNS = 4

# TEXT
FONT = "Helvetica"
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 32

STYLING = {
    "gap" : 0.5,
    "corner-radius" : 0 }

NUMBER_POSITIONS = {
    "." : {"column" : 2, "row" : 6, "span" : 1},
    0 : {"column" : 1, "row" : 6, "span" : 1},
    "00" : {"column" : 0, "row" : 6, "span" : 1},
    1 : {"column" : 0, "row" : 5, "span" : 1},
    2 : {"column" : 1, "row" : 5, "span" : 1},
    3 : {"column" : 2, "row" : 5, "span" : 1},
    4 : {"column" : 0, "row" : 4, "span" : 1},
    5 : {"column" : 1, "row" : 4, "span" : 1},
    6 : {"column" : 2, "row" : 4, "span" : 1},
    7 : {"column" : 0, "row" : 3, "span" : 1},
    8 : {"column" : 1, "row" : 3, "span" : 1},
    9 : {"column" : 2, "row" : 3, "span" : 1}
}

OPERATORS_POSTITIONS = {
    "/" : {"column" : 3, "row" : 2, "character" : "/"},
    "*" : {"column" : 3, "row" : 3, "character" : "x"},
    "-" : {"column" : 3, "row" : 4, "character" : "-"},
    "=" : {"column" : 3, "row" : 6, "character" : "="},
    "+" : {"column" : 3, "row" : 5, "character" : "+"}
}

OPERATIONS = {
    "clear" : {"column" : 0, "row" : 2, "text" : "AC"},
    "percentage" : {"column" : 2, "row" : 2, "text" : "%"},
    "underroot" : {"column" : 1, "row" : 2, "character" : "", "operator" : "math.sqrt", "image path" : {"light": "underroot light.png", "dark" : "underroot dark.png"}}
}

COLORS = {
    "light-gray" : {"fg": ("#505050","#D4D4D2"), "hover" : ("#686868", "#efefed"), "text" : ("white","black")},
    "dark-gray" : {"fg": ("#D4D4D2","#505050"), "hover": ("#efefed","#686868"), "text": ("black","white")},
    "orange" : {"fg": "#FF9500", "hover": "#ffb143", "text": ("black","white")},
    "orange-highlight" : {"fg": "white", "hover": "white", "text": ("black","#FF9500")}
    }

TITLE_BAR_HEX_COLORS = {
    "dark" : 0x00000000,
    "light" : 0x00EEEEEE
    }

BLACK = "#000000"
WHITE = "#EEEEEE"
