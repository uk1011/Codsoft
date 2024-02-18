from customtkinter import CTkButton
from setup import *

class Button(CTkButton):
    def __init__(self, parent, text, function, column, row, font, color = "dark-gray"):
        super().__init__(
            master = parent,
            command = function,
            text = text,
            corner_radius = STYLING["corner-radius"],
            font = font,
            fg_color = COLORS[color]["fg"],
            hover_color = COLORS[color]["hover"],
            text_color = COLORS[color]["text"]
        )

        self.grid(column = column, row = row, sticky = "NSEW")

class NumberButtons(Button):
    def __init__(self,parent, text, function, column, row, font,color = "light-gray"):
        super().__init__(
            parent = parent,
            text = text,
            function = lambda :function(text),
            column = column,
            row = row,
            font = font, 
            color = color)

class OperatorButtons(Button):
    def __init__(self,parent, text, operator, function, column, row, font,color = "orange"):
        super().__init__(
            parent = parent,
            text = text,
            function = lambda :function(operator),
            column = column,
            row = row,
            font = font, 
            color = color)

class ImageButton(CTkButton):
    def __init__(self,parent,function, column, row, image, text = "",color = "dark-gray"):
        super().__init__(
            master = parent,
            command = function,
            text = text,
            corner_radius = STYLING["corner-radius"],
            image = image,
            fg_color = COLORS[color]["fg"],
            hover_color = COLORS[color]["hover"],
            text_color = COLORS[color]["text"]
        )
        self.grid(column = column, row = row, sticky = "NSEW", padx = STYLING["gap"], pady = STYLING["gap"])