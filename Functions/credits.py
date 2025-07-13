import tkinter as tk  # Import the Tkinter library for graphical user interface
import json  # Import the JSON library to handle JSON files
from typing import Dict

# Load the JSON file containing localized or configurable texts
with open("keywords.json", "r", encoding="utf-8") as kw:
    keyword: Dict[str, Dict[str, str]] = json.load(kw)


def credits_text() -> None:
    """
    Creates a new Toplevel window that displays credit information.
    The text is built using f-string and values extracted from the JSON file.
    """
    # Create a secondary (Toplevel) window
    credit_window: tk.Toplevel = tk.Toplevel()

    # Set the title of the window
    credit_window.title("Credits")
    credit_window.iconbitmap("ewbIcon.ico")

    # Set fixed dimensions for the window (width x height)
    credit_window.geometry("780x25")

    # Construct the text to be displayed using f-string and data from the JSON file
    # This allows easy modification of content without changing the code
    developer: str = keyword['word']['developer']
    language: str = keyword['word']['language']
    tools: str = keyword['word']['tools']
    icon: str = keyword['word']['icon']

    full_text: str = (
        f"Developed by {developer} using {language} "
        f"and this tools {tools} and the {icon}"
    )

    credit_label: tk.Label = tk.Label(
        credit_window,
        text=full_text
    )

    # Position the label inside the window using basic layout manager
    credit_label.pack()