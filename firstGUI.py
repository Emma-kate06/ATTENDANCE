import tkinter as tk
from tkinter import messagebox

# --- 1. Define the action the button will perform ---
def show_output():
    """
    Retrieves text from the input box and displays it in the output label.
    """
    # Get the text currently in the Entry widget
    user_input = input_box.get()

    if user_input:
        # Update the text of the output_label
        output_label.config(text=f"You entered: {user_input}")
    else:
        # If the box is empty, show a message (optional)
        messagebox.showwarning("Empty Input", "Please enter some text!")
        output_label.config(text="Waiting for input...")

# --- 2. Set up the main window (Root) ---
root = tk.Tk()
root.title("Tkinter Basic App")
root.geometry("400x200") # Set a fixed size for the window

# --- 3. Create the Widgets (Components) ---

# Input Box (Entry)
input_label = tk.Label(root, text="Enter Text:")
input_label.pack(pady=5) # Adds padding above/below

input_box = tk.Entry(root, width=40)
input_box.pack(pady=5)

# Button
action_button = tk.Button(root, text="Click me!", command=show_output)
# The 'command' links the button click to the 'show_output' function
action_button.pack(pady=10)

# Output Label
output_label = tk.Label(root, text="Waiting for input...")
output_label.pack(pady=5)

# --- 4. Start the GUI event loop ---
# This keeps the window open and responsive to user actions
root.mainloop()