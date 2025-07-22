import tkinter as tk  # Import the Tkinter library for GUI
import pyperclip as pc  # Import pyperclip to copy text to clipboard
import json  # Import JSON library to handle JSON files
from functools import lru_cache as cache  # Import lru_cache and alias it as 'cache' for brevity
import traceback  # For detailed error output in case something breaks


@cache(maxsize=1)
def generate_github_text() -> str:
    """
    Retrieves and caches the GitHub URL from the JSON file.
    If the file is missing or invalid, returns a fallback error message.
    """
    try:
        with open("keywords.json", "r", encoding="utf-8") as kw:
            keyword = json.load(kw)
        return keyword["word"]["github"]
    except FileNotFoundError:
        return "Error: keywords.json not found."
    except json.JSONDecodeError:
        return "Error: Invalid JSON format."
    except KeyError:
        return "Error: 'github' key not found in JSON."
    except Exception:
        traceback.print_exc()
        return "Error: Unexpected issue while loading GitHub URL."


def github_text() -> None:
    """
    Creates a Toplevel window with a clickable label that copies the GitHub URL to the clipboard.
    Adds error handling for file, JSON, and clipboard access issues.
    """
    try:
        # Create a new popup window
        github_window: tk.Toplevel = tk.Toplevel()
        github_window.title("Github")

        # Attempt to set window icon (non-fatal if missing)
        try:
            github_window.iconbitmap("ewbIcon.ico")
        except Exception:
            print("Warning: Could not load window icon (ewbIcon.ico).")

        # Set fixed window size
        github_window.geometry("220x20")

        # Retrieve the GitHub URL (or error message)
        text: str = generate_github_text()

        # Create a clickable label
        github_label: tk.Label = tk.Label(github_window, text=text, cursor="hand2", fg="blue")
        github_label.pack()

        def auto_copy(event) -> None:
            """
            Copies the GitHub URL to the system clipboard when clicked.
            Handles clipboard errors gracefully.
            """
            try:
                pc.copy(text)
                github_label.config(fg="green")  # Visual feedback
                github_label.after(3000, lambda: github_label.config(fg="blue"))  # Reset color after 3 seconds
            except pc.PyperclipException:
                print("Clipboard error: Failed to copy to clipboard.")
                github_label.config(fg="red")
                github_label.after(3000, lambda: github_label.config(fg="blue"))

        # Bind left-click event
        github_label.bind("<Button-1>", auto_copy)

    except Exception:
        print("Error: Failed to create GitHub popup.")
        traceback.print_exc()
