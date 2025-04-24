# Eliya Statema
# 4/24/25
# Long-Distance Calls

import tkinter
import tkinter.messagebox

class Phone_Rate:
    def __init__(self):
        # Main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Telephone Rates")

        # Frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Radio Button Variable
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # Radio Buttons
        self.daytime_button = tkinter.Radiobutton(self.top_frame, text="Daytime - 6:00 A.M. through 5:59 P.M.",
                                                  variable=self.radio_var, value=1)
        self.evening_button = tkinter.Radiobutton(self.top_frame, text="Evening - 6:00 P.M.  through 11:59 P.M.",
                                                  variable=self.radio_var, value=2)
        self.offpeak_button = tkinter.Radiobutton(self.top_frame, text="Off-Peak - Midnight through 5:59 P.M.",
                                                  variable=self.radio_var, value=3)

        self.daytime_button.pack(anchor="w")
        self.evening_button.pack(anchor="w")
        self.offpeak_button.pack(anchor="w")

        # Prompt Label and Entry Widget
        self.prompt_label = tkinter.Label(self.middle_frame, text="Enter the number of minutes of the call: ")
        self.minutes_entry = tkinter.Entry(self.middle_frame, width=10)

        self.prompt_label.pack(side="left")
        self.minutes_entry.pack(side="left")

        # Calculate and Quit Buttons
        self.calculate_button = tkinter.Button(self.bottom_frame, text="Calculate Total", command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.calculate_button.pack(side="left", padx=5, pady=5)
        self.quit_button.pack(side="left", padx=5, pady=5)

        # Pack Frames
        self.top_frame.pack(padx=20, pady=10)
        self.middle_frame.pack(padx=20)
        self.bottom_frame.pack(pady=10)

        tkinter.mainloop()

    def calculate(self):
        if self.radio_var.get() == 1:
            rate = 0.02
        elif self.radio_var.get() == 2:
            rate = 0.12
        elif self.radio_var.get() == 3:
            rate = 0.05
        else:
            tkinter.messagebox.showinfo("Cost", f"Please select a rate category.")
        try:
            length = float(self.minutes_entry.get())
            cost = length * rate
            tkinter.messagebox.showinfo("Cost", f"TOTAL: ${cost:.2f}")
        except ValueError:
            tkinter.messagebox.showinfo("Error", f"You must enter the number of minutes.")

if __name__ == '__main__':
    GUI = Phone_Rate()