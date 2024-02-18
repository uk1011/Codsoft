import customtkinter as ctk
from buttons import Button, ImageButton, NumberButtons, OperatorButtons
import darkdetect
from PIL import Image
import math
from setup import *
try:
    from ctypes import windll, byref, sizeof, c_int
except :
    pass


class Calculator(ctk.CTk):
    def __init__(self,is_dark):
        
        super().__init__(fg_color = (WHITE, BLACK))
        #setting dark or light appearance depending on is_dark
        ctk.set_appearance_mode(f'{'dark' if is_dark else 'light'}')

        # change the title and change icon
        self.title("Calculator")
        self.iconbitmap("Calculator.ico")

        # setting window size and unabling window resizing
        self.geometry(f"{CALCULATOR_SIZE[0]}x{CALCULATOR_SIZE[1]}")
        self.resizable(False, False)
        self.title_bar_color(is_dark)

        # Grid Layout
        self.rowconfigure(list(range(ROWS)), weight = 1, uniform = "a")
        self.columnconfigure(list(range(COLUMNS)), weight = 1, uniform = "a")

        # data
        self.result_string = ctk.StringVar(value = "0")
        self.expression_string = ctk.StringVar(value = "")
        self.display_numbers = []
        self.full_operation = []

        # widgets
        self.create_widgets()

        self.mainloop()
    
    def create_widgets(self):

        # fonts
        main_font = ctk.CTkFont(family = FONT, size = NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family = FONT, size = OUTPUT_FONT_SIZE)

        # output label
        OutputLabel(self,0,"SE", main_font, self.expression_string)

        #experssions that will be evaluated
        OutputLabel(self,1,"E", result_font, self.result_string) # output answer

        # clear button
        Button(self, 
               text = OPERATIONS["clear"]["text"] , 
               function = self.clear_method,
               column = OPERATIONS["clear"]["column"], 
               row = OPERATIONS["clear"]["row"],
               font = main_font)

        # percentage button
        Button(self, 
               text = OPERATIONS["percentage"]["text"] , 
               function = self.percentage_method,
               column = OPERATIONS["percentage"]["column"], 
               row = OPERATIONS["percentage"]["row"],
               font = main_font)

        # underroot button
        underroot_image = ctk.CTkImage(
             light_image= Image.open(OPERATIONS["underroot"]["image path"]["dark"]),
             dark_image= Image.open(OPERATIONS["underroot"]["image path"]["light"],)
        )
        ImageButton(
             parent = self,
             function = self.underroot_method,
             column = OPERATIONS["underroot"]["column"],
             row = OPERATIONS["underroot"]["row"],
             image = underroot_image
        )

        # Number Buttons
        for number, data in NUMBER_POSITIONS.items():
             NumberButtons(
                  parent = self,
                  text = number,
                  function = self.number_press,
                  column = data["column"],
                  row = data["row"],
                  font = main_font
             )

        # operator buttons
        for operator, data in OPERATORS_POSTITIONS.items():
             OperatorButtons(
                  parent = self,
                  text = data["character"],
                  operator = operator,
                  function = self.operator_press,
                  column = data["column"],
                  row = data["row"],
                  font = main_font
             )

    # function when we press any number
    def number_press(self, value):
         self.display_numbers.append(str(value))
         full_number = "".join(self.display_numbers)
         self.result_string.set(full_number)

    # operator press
    def operator_press(self, value):
        current_number = "".join(self.display_numbers)

        if current_number:
            self.full_operation.append(current_number)
            
            if value != "=":
                #update data in expression string
                self.full_operation.append(value)
                self.display_numbers.clear()
                
                # updating the result
                self.result_string.set("")
                self.expression_string.set(" ".join(self.full_operation))
            
            else :
                expression = "".join(self.full_operation)
                result = eval(expression)

                # formatting the result
                if isinstance(result, float):
                      
                    #if result of integer is shown in float
                    if result.is_integer():
                        result = int(result)
                    else :
                        # too much large output in float
                        result = round(result, 4)
                          

                # update data
                self.full_operation.clear()
                self.display_numbers = [str(result)]


                # update the result
                self.result_string.set(result)
                self.expression_string.set(expression)


    # clear method
    def clear_method(self):
        # clear the output
        self.result_string.set(0)
        self.expression_string.set("")
        self.display_numbers.clear()
        self.full_operation.clear()

    # percentage method
    def percentage_method(self):
        if self.display_numbers:
            current_number = float("".join(self.display_numbers))
            percent_number = current_number/100

            #if result of integer is shown in float
            if percent_number.is_integer():
                percent_number = int(percent_number)
            else :
                # too much large output in float
                percent_number = round(percent_number, 4)

            # update data and Output
            self.display_numbers = list(str(percent_number))
            self.result_string.set("".join(self.display_numbers))

    # underroot method
    def underroot_method(self):
        current_number = "".join(self.display_numbers)
        if current_number:
            number = float(current_number)
            if number >= 0:
                result = math.sqrt(number)
                #if result of integer is shown in float
                if result.is_integer():
                    result = int(result)
                else :
                    # too much large output in float
                    result = round(result, 4)

                self.display_numbers.clear()
                self.display_numbers.append(str(result))
                self.result_string.set(result)
            else:
                self.result_string.set("error: negative number")


    def title_bar_color(self,is_dark):
            try:
                HWND = windll.user32.GetParent(self.winfo_id())
                DWMWA_ATTRIBUTE = 35
                COLOR = TITLE_BAR_HEX_COLORS['dark'] if is_dark else TITLE_BAR_HEX_COLORS['light']
                windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
            except:
                pass

class OutputLabel(ctk.CTkLabel):
     def __init__(self, parent,input_row, anchor, font, string_var):
          super().__init__(master=parent, font = font, textvariable = string_var)

          self.grid(column = 0, columnspan = 4, row = input_row, sticky = anchor, padx = 10)


if __name__ == "__main__":
    Calculator(darkdetect.isDark())