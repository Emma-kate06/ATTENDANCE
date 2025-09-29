import tkinter as tk
from tkinter import ttk

class FeedbackApp:
    """
    A simple GUI application using Tkinter for collecting customer feedback.
    """
    def __init__(self, master):
        self.master = master
        master.title("Customer Feedback App")

        # --- Configure styles and padding for better layout ---
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Inter', 10))
        style.configure('TButton', font=('Inter', 10, 'bold'))

        # Create a main frame with padding
        self.main_frame = ttk.Frame(master, padding="20 20 20 20")
        self.main_frame.pack(fill='both', expand=True)

        # 1. Main Title
        self.title_label = ttk.Label(
            self.main_frame,
            text="Please provide feedback on your experience.",
            font=('Inter', 16, 'bold'),
            foreground='#333333'
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 25), sticky='w')

        # --- Name Input ---
        self.name_label = ttk.Label(self.main_frame, text="Name:")
        self.name_label.grid(row=1, column=0, sticky='w', pady=5)

        self.name_entry = ttk.Entry(self.main_frame, width=50)
        self.name_entry.grid(row=1, column=1, sticky='ew', padx=10, pady=5)

        # --- Email Input ---
        self.email_label = ttk.Label(self.main_frame, text="Email:")
        self.email_label.grid(row=2, column=0, sticky='w', pady=5)

        self.email_entry = ttk.Entry(self.main_frame, width=50)
        self.email_entry.grid(row=2, column=1, sticky='ew', padx=10, pady=5)

        # --- Feedback Box (Large) ---
        self.feedback_label = ttk.Label(self.main_frame, text="Feedback:")
        self.feedback_label.grid(row=3, column=0, sticky='nw', pady=(15, 5))

        # Text widget for multi-line feedback
        self.feedback_text = tk.Text(self.main_frame, wrap='word', width=50, height=10, font=('Inter', 10), relief='solid', borderwidth=1)
        self.feedback_text.grid(row=3, column=1, sticky='ew', padx=10, pady=(15, 20))

        # --- Submit Button ---
        self.submit_button = ttk.Button(
            self.main_frame,
            text="Submit Feedback",
            command=self.submit_feedback,
            style='Accent.TButton'
        )
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Set column weights so the entry fields expand
        self.main_frame.grid_columnconfigure(1, weight=1)

    def submit_feedback(self):
        """
        Retrieves, prints, and clears the input data.
        """
        # Get data from entry boxes
        name = self.name_entry.get()
        email = self.email_entry.get()

        # Get data from Text box (must specify start '1.0' and end 'tk.END')
        # We use .strip() to remove trailing newline character
        feedback = self.feedback_text.get("1.0", tk.END).strip()

        # Print data to console
        print("="*40)
        print("      CUSTOMER FEEDBACK SUBMITTED      ")
        print("="*40)
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Feedback:\n{feedback}")
        print("-" * 40)
        print("Inputs cleared.")

        # Clear all input fields
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.feedback_text.delete("1.0", tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    app = FeedbackApp(root)
    root.mainloop()
