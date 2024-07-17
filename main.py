import os
import tkinter as tk

# Chemins des fichiers à modifier
file_path1 = "chemin/du/premier/fichier.txt"
file_path2 = "chemin/du/deuxieme/fichier.txt"

def set_read_only():
    global file_path1, file_path2

    os.chmod(file_path1, 0o444)  # Mettre en lecture seule le premier fichier
    os.chmod(file_path2, 0o444)  # Mettre en lecture seule le deuxième fichier

    status_label.config(text=f"Les fichiers sont maintenant en lecture seule.")

def remove_read_only():
    global file_path1, file_path2

    os.chmod(file_path1, 0o666)  # Enlever lecture seule du premier fichier
    os.chmod(file_path2, 0o666)  # Enlever lecture seule du deuxième fichier

    status_label.config(text=f"Les fichiers sont maintenant modifiables.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Modifier les permissions de fichiers")

# Boutons pour modifier les permissions
set_readonly_button = tk.Button(root, text="Mettre en lecture seule", command=set_read_only)
set_readonly_button.pack(pady=10)

remove_readonly_button = tk.Button(root, text="Enlever lecture seule", command=remove_read_only)
remove_readonly_button.pack(pady=10)

# Label pour afficher le statut
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()
