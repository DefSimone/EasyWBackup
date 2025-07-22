import tkinter as tk  # Import the Tkinter library for graphical user interface
import json  # Import the JSON library to handle JSON data
from functools import lru_cache as cache  # Import lru_cache for caching, aliasing it as 'cache'
from typing import Dict  # Import Dict type hint for structured typing
import traceback  # For detailed error messages in development/debugging


@cache(maxsize=1)
def generated_credit_text() -> str:
    """
    Generates the credit text using values from the JSON file.
    This function is decorated with lru_cache so that the result is cached after the first call.
    Only one version (maxsize=1) is stored since the result is static unless the file changes.
    """
    try:
        # Load the JSON file containing localized or configurable texts
        with open("keywords.json", "r", encoding="utf-8") as kw:
            keyword: Dict[str, Dict[str, str]] = json.load(kw)  # Parse the JSON into a nested dictionary

        # Extract individual values from the dictionary
        developer: str = keyword['word']['developer']
        language: str = keyword['word']['language']
        tools: str = keyword['word']['tools']
        icon: str = keyword['word']['icon']

        # Format and return the credit string
        return f"Developed by {developer} using {language}, tools: {tools}, and the {icon} icon"

    except FileNotFoundError:
        return "Error: keywords.json file not found."
    except json.JSONDecodeError:
        return "Error: Failed to parse keywords.json."
    except KeyError as e:
        return f"Error: Missing key in JSON file: {e}"
    except Exception:
        # For any other unexpected errors
        traceback.print_exc()
        return "An unexpected error occurred while generating credits."


def credit_text() -> None:
    """
    Creates a new Toplevel window that displays credit information.
    The text is generated using a cached function to improve performance and avoid re-reading the file.
    """
    try:
        # Create a secondary (popup) window separate from the main application
        credit_window: tk.Toplevel = tk.Toplevel()
        credit_window.title("Credits")

        # Set a custom icon for the window (the file must exist in the same directory)
        try:
            credit_window.iconbitmap("ewbIcon.ico")
        except Exception:
            print("Warning: Failed to load icon 'ewbIcon.ico'.")

        # Set fixed dimensions for the window: 780 pixels wide and 25 pixels tall
        credit_window.geometry("780x25")

        # Retrieve the credit text (cached after the first read from the JSON file)
        text: str = generated_credit_text()

        # Create a label widget containing the credit text
        credit_label: tk.Label = tk.Label(credit_window, text=text)
        credit_label.pack()

    except Exception:
        # In case the GUI fails entirely
        print("Failed to display the credit popup.")
        traceback.print_exc()
