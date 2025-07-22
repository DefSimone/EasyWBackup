import tkinter as tk  # Tkinter for GUI

# Import custom functions from the local package structure
from Functions.credit import credit_text
from Functions.linkedin import linkedin_text
from Functions.github import github_text
from Functions.help import help_text
from Functions.cache import clear_all_caches

def main():
    try:
        # Create the main window
        window = tk.Tk()
        window.title("EasyWBackup")

        # Try to set the custom window icon (non-critical if it fails)
        try:
            window.iconbitmap("ewbIcon.ico")
        except Exception as e:
            print(f"Warning: Could not load icon 'ewbIcon.ico'. Details: {e}")

        # Maximize the window (Windows only, 'zoomed' may not work on Linux/macOS)
        window.state('zoomed')

        # Create the menu bar
        menu = tk.Menu(window)
        window.config(menu=menu)

        # --- Options Menu ---
        options_menu = tk.Menu(menu, tearoff=0)
        options_menu.add_command(label="Backup Once")        # Placeholder (add command later)
        options_menu.add_command(label="Backup Schedule")    # Placeholder
        options_menu.add_command(label="Sync Backup")        # Placeholder
        menu.add_cascade(label="Options", menu=options_menu)

        # --- Actions Menu ---
        actions_menu = tk.Menu(menu, tearoff=0)
        actions_menu.add_command(label="Delete Cache", command=clear_all_caches)
        actions_menu.add_command(label="Help", command=help_text)
        menu.add_cascade(label="Actions", menu=actions_menu)

        # --- Utility Menu ---
        utility_menu = tk.Menu(menu, tearoff=0)
        utility_menu.add_command(label="Log Reader")         # Placeholder
        utility_menu.add_command(label="Log Exporter")       # Placeholder
        menu.add_cascade(label="Utility", menu=utility_menu)

        # --- About Menu ---
        about_menu = tk.Menu(menu, tearoff=0)
        about_menu.add_command(label="Github", command=github_text)
        about_menu.add_command(label="Linkedin", command=linkedin_text)
        about_menu.add_command(label="Credits", command=credit_text)
        menu.add_cascade(label="About", menu=about_menu)

        # Start the main event loop
        window.mainloop()

    except Exception as e:
        print(f"Fatal error: Unable to start application. Details: {e}")

# Only run main if this file is executed directly
if __name__ == "__main__":
    main()
