# Connection à une BD
# Il faut avoir installé mysqlconnector (pip install mysql-connector-python)
# Author : Jaruphong et Gaëtan
# Version 1.0 Date : 10.06.2025

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importer Themed Tkinter, widgets pour améliorer l'affiche

import model  # Import du fichier contenant les fonctions d'accès à la BD

tree = None

def refresh_participant():
    """Rafraîchit l'affichage des courses."""
    global tree
    for widget in frame.winfo_children():
        widget.destroy()  # Supprime tous les widgets pour recréer la liste

    participants = model.read_table("participants")  # Récupère les cours depuis la BD

    if not participants:
        tk.Label(frame, text="Aucun participant trouvé.", font=("Arial", 12)).pack()
        tree = None
        return

    columns = ("id", "first_name", "last_name", "phone", "mail")
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Définir les titres des colonnes
    tree.heading("id", text="ID")
    tree.heading("first_name", text="Prénom")
    tree.heading("last_name", text="Nom de famille")
    tree.heading("phone", text="No Téléphone")
    tree.heading("mail", text="Mail")

    # Ajuster la largeur
    for col in columns:
        tree.column(col, width=100)

    # Remplir le tabeau
    for part in participants:
        # Ajouter une ligne dans le tableau Treeview,
        # "" ajouter l'élément à la racine (pas dans un groupe hiérarchique)
        # "end" ajouter à la fin de la liste actuelle
        # values=(...), les données de chaque colonne
        tree.insert("", "end", values=(
            part["id"],
            part["first_name"],
            part["last_name"],
            part["phone"],
            part["mail"],
        ))

    # Affiche ce tableau, utilise tout l'espace
    tree.pack(fill="both", expand=True)

def add_participant():
    """Ajoute un participant à la base de données."""
    last_name = entry_last_name.get().strip()
    first_name = entry_first_name.get().strip()
    phone = entry_phone.get().strip()
    mail = entry_mail.get().strip()

    if not last_name or not first_name or not phone or not mail:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs !")
        return

    success = model.insert_row("participants", {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "mail": mail,
    })
    if success:
        messagebox.showinfo("Succès", "Compte créé avec succès !")
        entry_first_name.delete(0, tk.END)
        entry_last_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_mail.delete(0, tk.END)
        refresh_participant()
    else:
        messagebox.showerror("Erreur", "Impossible de créer le compte.")

def delete_inscription(tree):
    """Supprime une inscription sélectionnée dans le treeview."""
    if not tree:
        messagebox.showerror("Erreur", "Aucune liste affichée.")
        return

    selection = tree.selection()

    if not selection:
        messagebox.showwarning("Aucun élément sélectionné", "Veuillez sélectionner une inscription à supprimer.")
        return

    # On suppose que l'ID est dans la première colonne
    item = tree.item(selection[0])
    values = item["values"]
    # Afficher la fenêtre avec le text qui contient le prénom d'inscripstion, le cours
    insc_id = values[0] # pour supprimer avec id
    prenom = item["values"][1]

    if messagebox.askyesno("Confirmation", f"Supprimer l'inscription de {prenom}?"):
        try:
            model.delete_row("Participants_has_cook_courses", {"id": insc_id})
            refresh_participant()
            messagebox.showinfo("Succès", "inscription supprimée")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreeur de la suppression :{e}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Nouveau membre")
root.geometry("700x400")

form_frame = tk.Frame(root, pady=10)
form_frame.pack(fill="x")

tk.Label(form_frame, text="Prénom :", font=("Arial", 12)).grid(row=0, column=0, padx=4, pady=2)
entry_first_name = tk.Entry(form_frame, font=("Arial", 12))
entry_first_name.grid(row=0, column=1, padx=4, pady=2)

tk.Label(form_frame, text="Nom :", font=("Arial", 12)).grid(row=0, column=2, padx=4, pady=2)
entry_last_name = tk.Entry(form_frame, font=("Arial", 12))
entry_last_name.grid(row=0, column=3, padx=4, pady=2)

tk.Label(form_frame, text="Téléphone :", font=("Arial", 12)).grid(row=1, column=0, padx=4, pady=2)
entry_phone = tk.Entry(form_frame, font=("Arial", 12))
entry_phone.grid(row=1, column=1, padx=4, pady=2)

tk.Label(form_frame, text="Mail :", font=("Arial", 12)).grid(row=1, column=2, padx=4, pady=2)
entry_mail = tk.Entry(form_frame, font=("Arial", 12))
entry_mail.grid(row=1, column=3, padx=4, pady=2)

# Le bouton va permettre d'ajouter simplement les informations du membres à la base de donnée.

btn_add = tk.Button(form_frame, text="Nouveau inscrit", command=add_participant, bg="green", fg="white")
btn_add.grid(row=2, column=1, pady=5, padx=5)

btn_delete = tk.Button(form_frame, text="Supprimer", command=lambda :delete_inscription(tree), bg="red", fg="white")
btn_delete.grid(row =2, column=2, pady=5, padx=5)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)
refresh_participant()

# Lancer l'application
root.mainloop()