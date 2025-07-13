import tkinter as tk  # Import the Tkinter library for GUI
import pyperclip as pc  # Import pyperclip to copy text to clipboard
import json  # Import JSON library to handle JSON files

# Load localized or configurable texts from JSON file
with open("keywords.json", "r", encoding="utf-8") as kw:
    keyword: dict[str, dict[str, str]] = json.load(kw)


def github_text() -> None:
    """
    Creates a Toplevel window with a clickable label that copies a GitHub URL to the clipboard.
    The URL is taken from the JSON file to allow easy updates without modifying code.
    """
    # Create a new Toplevel window
    github_window: tk.Toplevel = tk.Toplevel()

    # Set the title of the window
    github_window.title("Github")
    github_window.iconbitmap("ewbIcon.ico")

    # Set fixed dimensions for the window (width x height)
    github_window.geometry("220x20")

    # Get the LinkedIn URL from the JSON data
    text: str = keyword["word"]["github"]

    # Create a Label widget to display the GitHub URL
    github_label: tk.Label = tk.Label(github_window, text=text)
    github_label.pack()

    def auto_copy(event) -> None:
        """
        Copies the GitHub URL to the system clipboard when the label is clicked.
        """
        pc.copy(text)  # Copy the URL to clipboard using pyperclip [[4]]

    # Bind the left mouse click event to the auto_copy function
    github_label.bind("<Button-1>", auto_copy)