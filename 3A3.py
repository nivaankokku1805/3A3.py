from tkinter import *

# Function to convert inches to centimeters
def convert_to_cm():
    try:
        inches = float(entry_value.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except ValueError:
        result_label.config(text="Invalid input!")

# Create main window
window = Tk()
window.title("Inches to Centimeters Converter")
window.geometry("350x200")

# Input label and entry
input_label = Label(window, text="Enter length in inches:")
input_label.pack(pady=10)

entry_value = StringVar()
entry_field = Entry(window, textvariable=entry_value)
entry_field.pack(pady=5)

# Convert button
convert_button = Button(window, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)

# Result label
result_label = Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Exit button
exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.pack(pady=5)

# Run the application
window.mainloop()