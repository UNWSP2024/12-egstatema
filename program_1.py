# Eliya Statema
# 4/23/25
# MPG Calculator

import tkinter
import tkinter.messagebox

class MPG_Calculator_GUI:
    def __init__(self):
        # Create main window and frames
        self.main_window = tkinter.Tk()
        self.main_window.title("MPG Calculator")
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the label and entry widgets
        self.gas_prompt_label = tkinter.Label(self.top_frame, text="Enter the number of gallons of gas the car holds: ")
        self.gas_entry = tkinter.Entry(self.top_frame, width=10)
        self.miles_prompt_label = tkinter.Label(self.middle_frame, text="Enter the number of miles the car can drive on a full tank: ")
        self.miles_entry = tkinter.Entry(self.middle_frame, width=10)

        # Pack the widgets
        self.gas_prompt_label.pack(side="left")
        self.gas_entry.pack(side="left")
        self.miles_prompt_label.pack(side="left")
        self.miles_entry.pack(side="left")

        # Create button widgets
        self.calculate_button = tkinter.Button(self.bottom_frame, text="Calculate MPG", command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack the buttons
        self.calculate_button.pack(side="left", padx=5, pady=5)
        self.quit_button.pack(side="left", padx=5, pady=5)

        # Pack the frames
        self.top_frame.pack(ipadx=5, ipady=5)
        self.middle_frame.pack(ipadx=5, ipady=5)
        self.bottom_frame.pack(ipadx=5, ipady=5)

        # Enter the mainloop
        tkinter.mainloop()

    def calculate(self):
        try:
            gas = float(self.gas_entry.get())
            miles = float(self.miles_entry.get())
            MPG = miles / gas
            tkinter.messagebox.showinfo("Results", f"This vehicle can drive {MPG:.1f} miles per gallon.")
        except ValueError:
            tkinter.messagebox.showinfo("Error", f"Please enter valid integers.")
        except ZeroDivisionError:
            tkinter.messagebox.showinfo("Error", f"You cannot use zero.")

if __name__ == '__main__':
    MPG_Calculator = MPG_Calculator_GUI()