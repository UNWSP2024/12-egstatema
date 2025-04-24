# Eliya Statema
# 4/23/25
# Joe's Automotive

import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        # Main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")

        # Frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # IntVar
        self.oil_change = tkinter.IntVar()
        self.lube_job = tkinter.IntVar()
        self.radiator_flush = tkinter.IntVar()
        self.transmission_fluid = tkinter.IntVar()
        self.inspection = tkinter.IntVar()
        self.muffler = tkinter.IntVar()
        self.tire_rotation = tkinter.IntVar()

        self.oil_change.set(0)
        self.lube_job.set(0)
        self.radiator_flush.set(0)
        self.transmission_fluid.set(0)
        self.inspection.set(0)
        self.muffler.set(0)
        self.tire_rotation.set(0)

        # Checkbuttons
        self.oil_change_button = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30.00', variable=self.oil_change)
        self.lube_job_button = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20.00', variable=self.lube_job)
        self.radiator_flush_button = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', variable=self.radiator_flush)
        self.transmission_fluid_button = tkinter.Checkbutton(self.top_frame, text='Transmission Fluid - $100.00', variable=self.transmission_fluid)
        self.inspection_button = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', variable=self.inspection)
        self.muffler_button = tkinter.Checkbutton(self.top_frame, text='Muffler Replacement - $200.00', variable=self.muffler)
        self.tire_rotation_button = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', variable=self.tire_rotation)

        self.oil_change_button.pack(anchor="w")
        self.lube_job_button.pack(anchor="w")
        self.radiator_flush_button.pack(anchor="w")
        self.transmission_fluid_button.pack(anchor="w")
        self.inspection_button.pack(anchor="w")
        self.muffler_button.pack(anchor="w")
        self.tire_rotation_button.pack(anchor="w")

        # Calculate and Quit Buttons
        self.calculate_button = tkinter.Button(self.bottom_frame, text="Calculate Total", command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.calculate_button.pack(side="left", padx=5, pady=5)
        self.quit_button.pack(side="left", padx=5, pady=5)

        # Pack Frames
        self.top_frame.pack(padx=20, pady=20)
        self.bottom_frame.pack()

        # Enter mainloop
        tkinter.mainloop()

    # Add up checked boxes
    def calculate(self):
        total = 0
        if self.oil_change.get() == 1:
            total += 30
        if self.lube_job.get() == 1:
            total += 20
        if self.radiator_flush.get() == 1:
            total += 40
        if self.transmission_fluid.get() == 1:
            total += 100
        if self.inspection.get() == 1:
            total += 35
        if self.muffler.get() == 1:
            total += 200
        if self.tire_rotation.get() == 1:
            total += 20
        if total == 0:
            tkinter.messagebox.showinfo("Total", "No services have been selected.")
        else:
            tkinter.messagebox.showinfo("Total", f"TOTAL: ${total:.2f}")

if __name__ == '__main__':
    JoesAutomotive = GUI()