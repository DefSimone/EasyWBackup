import tkinter as tk
from Functions.credits import credits_text
from Functions.linkedin import linkedin_text
from Functions.github import github_text

window = tk.Tk()
window.iconbitmap("ewbIcon.ico")
window.title("EasyWBackup")
window.state('zoomed')
menu = tk.Menu(window)
window.config (menu=menu)

options_menu = tk.Menu(menu, tearoff=0)
options_menu.add_command(label="Backup Once")
options_menu.add_command(label="Backup Schedule")
options_menu.add_command(label="Sync Backup")
menu.add_cascade(label="Options", menu=options_menu)


actions_menu = tk.Menu(menu, tearoff=0)
actions_menu.add_command(label="Delete Cache")
actions_menu.add_command(label="Help")
menu.add_cascade(label="Actions", menu=actions_menu)

utility_menu = tk.Menu(menu, tearoff=0)
utility_menu.add_command(label="Log Reader")
utility_menu.add_command(label="Log Exporter")
menu.add_cascade(label="Utility", menu=utility_menu)

about_menu = tk.Menu(menu, tearoff=0)
about_menu.add_command(label="Github", command=github_text)
about_menu.add_command(label="Linkedin", command=linkedin_text)
about_menu.add_command(label="Credits", command=credits_text)
menu.add_cascade(label="About", menu=about_menu)

window.mainloop()