import tkinter as tk

def greet():
    name = entry.get()
    label_output.config(text=f"Hello, {name}! Welcome to Tkinter.")

# Create main window
window = tk.Tk()
window.title("Simple Tkinter App")
window.geometry("300x200")

# Create widgets
label_title = tk.Label(window, text="Enter your name:", font=("Arial", 12))
label_title.pack(pady=10)

entry = tk.Entry(window, width=25)
entry.pack(pady=5)

button = tk.Button(window, text="Greet Me", command=greet)
button.pack(pady=10)

label_output = tk.Label(window, text="", font=("Arial", 12), fg="blue")
label_output.pack(pady=10)

# Run the GUI loop
window.mainloop()
