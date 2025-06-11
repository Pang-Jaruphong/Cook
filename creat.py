# Connection à une BD
# Il faut avoir installé mysqlconnector (pip install mysql-connector-python)
# Author : Jaruphong et Gaëtan
# Version 1.0 Date : 10.06.2025

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importer Themed Tkinter, widgets pour améliorer l'affiche
import model  # Import du fichier contenant les fonctions d'accès à la BD
import subprocess

tree = None


def add_participant():
    """Ajoute un participant à la base de données."""
    last_name = entry_last_name.get().strip()
    first_name = entry_first_name.get().strip()
    phone = entry_phone.get().strip()
    mail = entry_mail.get().strip()

    if not last_name or not mail:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs !")
        return

    success = model.insert_row("participants", {
        "last_name": last_name,
        "first_name": first_name,
        "phone": phone,
        "mail": mail,
    })
    if success:
        messagebox.showinfo("Succès", "Compte créé avec succès !")
        last_name.delete(0, tk.END)
        mail.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Impossible de créer le compte.")

def update_participant():
    """modifie un participant existant."""
    last_name = entry_last_name.get().strip()
    first_name = entry_first_name.get().strip()
    phone = entry_phone.get().strip()
    mail = entry_mail.get().strip()

    if not last_name or not mail:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs !")
        return

    success = model.update_participant_info("participants", {
        "last_name": last_name,
        "first_name": first_name,
        "phone": phone,
        "mail": mail,
    }, last_name, first_name)
    if success:
        messagebox.showinfo("Succès", "Compte créé avec succès !")
        last_name.delete(0, tk.END)
        mail.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Impossible de créer le compte.")




# Création de la fenêtre principale
root = tk.Tk()
root.title("Nouveau membre")
root.geometry("900x300")

form_frame = tk.Frame(root, pady=10)
form_frame.pack(fill="x")

tk.Label(form_frame, text="Nom :", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=2)
entry_last_name = tk.Entry(form_frame, font=("Arial", 12))
entry_last_name.grid(row=0, column=1, padx=5, pady=2)

tk.Label(form_frame, text="Prenom :", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=2)
entry_first_name = tk.Entry(form_frame, font=("Arial", 12))
entry_first_name.grid(row=1, column=1, padx=5, pady=2)

tk.Label(form_frame, text="Téléphone :", font=("Arial", 12)).grid(row=1, column=3, padx=5, pady=2)
entry_phone = tk.Entry(form_frame, font=("Arial", 12))
entry_phone.grid(row=1, column=4, padx=5, pady=2)

tk.Label(form_frame, text="Mail :", font=("Arial", 12)).grid(row=0, column=3, padx=5, pady=2)
entry_mail = tk.Entry(form_frame, font=("Arial", 12))
entry_mail.grid(row=0, column=4, padx=5, pady=2)

# Le bouton va permettre d'ajouter simplement les informations du membres à la base de donnée.

btn_add = tk.Button(form_frame, text="Créer", command=add_participant, bg="green", fg="white")
btn_add.grid(row=2, columnspan=1, pady=5, padx=5)

# Le bouton va permettre d'ajouter simplement les informations du membres à la base de donnée.

btn_add = tk.Button(form_frame, text="Update", command=update_participant, bg="green", fg="white")
btn_add.grid(row=2, columnspan=1, pady=5, padx=5)


# Lancer l'application
root.mainloop()