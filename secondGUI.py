import tkinter as tk
from tkinter import font as tkfont
from functools import partial

class TranslatorApp:
    """
    A simple Python Tkinter application to translate 'Hello' into four languages.

    The application uses a class structure (OOP) to manage the GUI components
    and logic cleanly.
    """
    def __init__(self, master):
        """
        Initializes the main application window and its components.
        :param master: The root Tkinter window.
        """
        self.master = master
        master.title("Greeting Translator")
        # Reduced window size to fit content more tightly
        master.geometry("350x250")
        
        # Configure grid column to expand in the center for better centering
        master.grid_columnconfigure(0, weight=1)

        # --- 1. Define the translation data ---
        self.translations = {
            # Key (English Name): Value (Greeting)
            "Spanish": "Hola",
            "French": "Bonjour",
            "German": "Hallo",
            "English": "Hello"
        }
        
        # Define native labels for button display
        self.native_labels = {
            # Key (English Name): Value (Native Label)
            "Spanish": "Español",
            "French": "Français",
            "German": "Deutsch",
            "English": "English"
        }

        # --- 2. Setup Fonts ---
        self.title_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        self.greeting_font = tkfont.Font(family="Arial", size=30, weight="bold")
        self.button_font = tkfont.Font(family="Helvetica", size=10)

        # --- 3. Create GUI Elements ---

        # Welcome and Prompt Label (Vertical padding reduced from 20 to 10 and 10 to 5)
        self.prompt_label = tk.Label(
            master,
            text="Welcome to the Translator!\nSelect a language to see the greeting:",
            font=self.title_font,
            pady=15,
        )
        self.prompt_label.grid(row=0, column=0, pady=(10, 5))

        # Greeting Output Label (Vertical padding reduced from 10 to 5 and 20 to 10)
        self.greeting_text = tk.StringVar(value=self.translations["English"])
        
        self.greeting_label = tk.Label(
            master,
            textvariable=self.greeting_text,
            font=self.greeting_font,
        )
        self.greeting_label.grid(row=1, column=0, pady=(5, 10))

        # Button Container Frame (Padding reduced from 10 to 5)
        # This frame will now hold buttons stacked vertically
        button_frame = tk.Frame(master)
        button_frame.grid(row=2, column=0, pady=5)

        # --- 4. Create and Place Buttons ---
        
        for lang_key, greeting in self.translations.items():
            # Get the native language label for the button text
            button_label = self.native_labels.get(lang_key, lang_key)
            
            # Create a function that calls self.translate with the specific language key.
            # partial() is used here to pass arguments to the command function.
            command_func = partial(self.translate, lang_key)
            
            # Create the button (Colors removed)
            button = tk.Button(
                button_frame,
                text=button_label, # Use the native language label
                command=command_func,
                font=self.button_font,
                relief=tk.RAISED,
                padx=10,
                pady=3, # Reduced internal vertical padding for buttons
                width=10
            )
            # Place the button in the frame (using pack() without side=LEFT stacks them vertically by default)
            button.pack(padx=5, pady=3) # Reduced external vertical padding for buttons


    def translate(self, language_key):
        """
        Updates the main greeting label with the translation for the selected language.
        
        :param language_key: The string key (e.g., "Spanish") for the language.
        """
        # Look up the greeting using the key
        new_greeting = self.translations.get(language_key, "Error: Translation Not Found")
        
        # Update the StringVar associated with the greeting_label
        self.greeting_text.set(new_greeting)
        
        # Update the prompt to show what was clicked
        self.prompt_label.config(text=f"Greeting in {language_key}:")


if __name__ == '__main__':
    # 1. Create the root window
    root = tk.Tk()
    
    # 2. Instantiate the application class, passing the root window as the master
    app = TranslatorApp(root)
    
    # 3. Start the main event loop
    root.mainloop()