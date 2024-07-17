import os
import tkinter as tk
from tkinter import filedialog

def set_read_only():
    filepath = filedialog.askopenfilename()
    if filepath:
        os.chmod(filepath, 0o444)  # Octal 444 means read-only for everyone
        status_label.config(text=f"Le fichier {filepath} est maintenant en lecture seule.")

def remove_read_only():
    filepath = filedialog.askopenfilename()
    if filepath:
        os.chmod(filepath, 0o666)  # Octal 666 means read-write for everyone
        status_label.config(text=f"Le fichier {filepath} est maintenant modifiable.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Modifier les permissions de fichier")

# Création des boutons
set_readonly_button = tk.Button(root, text="Mettre en lecture seule", command=set_read_only)
remove_readonly_button = tk.Button(root, text="Enlever lecture seule", command=remove_read_only)

# Placement des boutons
set_readonly_button.pack(pady=10)
remove_readonly_button.pack(pady=10)

# Label pour afficher le statut
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()
