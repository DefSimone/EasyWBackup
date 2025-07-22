import tkinter as tk  # Import the Tkinter library to build GUI windows
import gc  # Import the garbage collector module to inspect objects in memory
import traceback  # for detailed error logging


def clear_all_caches() -> None:
    """
    Scans all live Python objects and clears the cache of any function
    decorated with @lru_cache (i.e., functions with a built-in cache).
    """
    try:
        for obj in gc.get_objects():
            # Check if the object is callable (likely a function) and has the typical methods of an LRU-cached function
            if callable(obj) and hasattr(obj, 'cache_clear') and hasattr(obj, 'cache_info'):
                try:
                    obj.cache_clear()  # Attempt to clear the cache of the function
                except TypeError:
                    # Some functions might throw a TypeError if called improperly; skip them
                    continue
    except Exception:
        print("An unexpected error occurred while clearing caches:")
        traceback.print_exc()  #shows detailed stack trace in the console/log
    show_cache_cleared_popup()

def show_cache_cleared_popup() -> None:
    """
    Displays a simple popup window informing the user that the cache was cleared successfully.
    If setting the icon fails (e.g., missing file), the rest of the popup still works.
    """
    try:
        popup: tk.Toplevel = tk.Toplevel()  # Create a new top-level (popup) window separate from the main window
        popup.title("Cache Cleared")  # Set the window title
        popup.geometry("300x100")  # Define the window size in pixels (width x height)

        try:
            popup.iconbitmap("ewbIcon.ico")  # Set a custom icon for the window
        except Exception:
            print("Warning: Failed to load custom window icon (ewbIcon.ico).")  # Soft fail

        # Create a label widget with the confirmation message and custom font
        label: tk.Label = tk.Label(popup, text="Cache successfully deleted.", font=("Arial", 12))
        label.pack(pady=20)  # Place the label in the window with vertical padding

        # Create an "OK" button that closes the popup when clicked
        close_button: tk.Button = tk.Button(popup, text="OK", command=popup.destroy)
        close_button.pack()  # Place the button in the popup window

    except Exception:
        # If the GUI cannot be shown at all, at least print something
        print("Failed to display the cache cleared popup.")
        traceback.print_exc()
