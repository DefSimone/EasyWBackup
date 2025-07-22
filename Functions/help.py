import tkinter as tk  # Import the Tkinter library for graphical user interface
from functools import lru_cache as cache  # Import lru_cache and alias it for readability
import traceback  # For detailed error logging in case of unexpected issues


@cache(maxsize=1)
def generate_help_text() -> str:
    """
    Returns a static help message string, describing the available backup options.
    The result is cached to avoid redundant computation, even if minimal in this case.
    """
    return (
        "Backup Once = This function allows you to select a single source path and multiple destination paths "
        "to back up your files one time.\n"
        "Backup Scheduled = This function allows you to select a single source path and multiple destination paths "
        "to back up your files daily, weekly, monthly, or annually.\n"
        "Sync Backup = This function allows you to select a single source path and multiple destination paths "
        "to monitor and back up your files whenever changes occur."
    )


def help_text() -> None:
    """
    Creates a new popup (Toplevel) window that displays help information about backup modes.
    Uses a cached function to retrieve the help text for performance and consistency.
    Handles potential runtime errors gracefully and logs them to the console.
    """
    try:
        # Create a Toplevel window (i.e., a popup above the main GUI)
        help_window: tk.Toplevel = tk.Toplevel()
        help_window.title("Help")

        # Attempt to load a custom window icon (non-fatal if missing)
        try:
            help_window.iconbitmap("ewbIcon.ico")
        except Exception:
            print("Warning: Could not load icon 'ewbIcon.ico'.")

        # Set fixed window size
        help_window.geometry("900x100")

        # Create a label widget with the help text
        help_label: tk.Label = tk.Label(
            help_window,
            text=generate_help_text(),
            justify="left",      # Align multiline text to the left
            anchor="w",          # Anchor text to the west (left side)
            wraplength=880       # Prevent text from overflowing the window
        )

        # Place the label inside the window with padding
        help_label.pack(padx=10, pady=10)

    except Exception:
        print("Error: Failed to display help window.")
        traceback.print_exc()
