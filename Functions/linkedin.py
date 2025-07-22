import tkinter as tk  # Import the Tkinter library for GUI
import pyperclip as pc  # Import pyperclip to copy text to clipboard
import json  # Import JSON library to handle JSON files
import traceback  # Import traceback to print detailed error logs for unexpected issues


def generate_linkedin_text() -> str:
    """
    Attempts to load the LinkedIn URL from a local JSON file.
    Returns a descriptive error string if the file is missing or malformed.
    """
    try:
        with open("keywords.json", "r", encoding="utf-8") as kw:
            keyword: dict[str, dict[str, str]] = json.load(kw)
        return keyword["word"]["linkedin"]
    except FileNotFoundError:
        return "Error: keywords.json not found."
    except json.JSONDecodeError:
        return "Error: Invalid JSON format in keywords.json."
    except KeyError:
        return "Error: 'linkedin' key not found in JSON."
    except Exception:
        traceback.print_exc()
        return "Error: Unexpected issue while reading keywords.json."


def linkedin_text() -> None:
    """
    Creates a Toplevel window with a clickable label.
    On click, it copies the LinkedIn URL (from JSON) to the clipboard.
    Handles and logs errors gracefully, with basic visual feedback.
    """
    try:
        # Create a new Toplevel (popup) window
        linkedin_window: tk.Toplevel = tk.Toplevel()
        linkedin_window.title("LinkedIn")

        # Try setting a custom icon (non-fatal if missing)
        try:
            linkedin_window.iconbitmap("ewbIcon.ico")
        except Exception as e:
            print(f"Warning: Could not load icon 'ewbIcon.ico'. Details: {e}")

        # Set fixed dimensions for the popup window
        linkedin_window.geometry("220x20")

        # Retrieve the LinkedIn URL or an error message
        text: str = generate_linkedin_text()

        # If the text is an error, make it red, else use blue
        label_color = "red" if text.startswith("Error:") else "blue"

        # Create the label widget with the URL or error text
        linkedin_label: tk.Label = tk.Label(
            linkedin_window,
            text=text,
            fg=label_color,
            cursor="hand2"
        )
        linkedin_label.pack()

        def auto_copy(event) -> None:
            """
            Copies the LinkedIn URL to the clipboard when the label is clicked.
            Shows visual feedback (green on success, red on failure).
            Does not attempt to copy if the label contains an error message.
            """
            if text.startswith("Error:"):
                print("Copy aborted: error message cannot be copied.")
                linkedin_label.config(fg="orange")  # Feedback color for skipped action
                linkedin_label.after(3000, lambda: linkedin_label.config(fg=label_color))
                return

            try:
                pc.copy(text)
                linkedin_label.config(fg="green")  # Feedback on success
                linkedin_label.after(3000, lambda: linkedin_label.config(fg="blue"))
            except pc.PyperclipException as e:
                print(f"Clipboard error: {e}")
                linkedin_label.config(fg="red")
                linkedin_label.after(3000, lambda: linkedin_label.config(fg=label_color))

        # Bind left mouse click to the copy function
        linkedin_label.bind("<Button-1>", auto_copy)

    except Exception as e:
        print(f"Fatal error: Failed to create LinkedIn popup window. Details: {e}")
        traceback.print_exc()
