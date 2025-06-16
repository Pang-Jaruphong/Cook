# Connection à une BD
# Il faut avoir installé mysqlconnector (pip install mysql-connector-python)
# Author : Jaruphong et Gaëtan
# Version 1.0 Date : 10.06.2025

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess

import model  # module d'accès à la BD
# Variable globale pour le treeview
tree = None

def refresh_participants_courses():
    """Affiche les inscriptions (participants à des cours)."""
    global tree
    for widget in frame.winfo_children():
        widget.destroy()

    inscriptions = model.get_participants_courses()

    if not inscriptions:
        tk.Label(frame, text="Aucune inscription trouvée.", font=("Arial", 12)).pack()
        tree = None
        return

    columns = ("id", "first_name", "last_name", "course_name")
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Définir les titres des colonnes
    tree.heading("id", text="ID")
    tree.heading("first_name", text="Nom")
    tree.heading("last_name", text="Prénom")
    tree.heading("course_name", text="Cours")

    # Ajuster la largeur
    for col in columns:
        tree.column(col, width=100)

    # Remplir le tabeau
    for participant in inscriptions:
        # Ajouter une ligne dans le tableau Treeview,
        # "" ajouter l'élément à la racine (pas dans un groupe hiérarchique)
        # "end" ajouter à la fin de la liste actuelle
        # values=(...), les données de chaque colonne
        tree.insert("", "end", values=(
            participant["id"],
            participant["first_name"],
            participant["last_name"],
            participant["course_name"],
        ))

    # Affiche ce tableau, utilise tout l'espace
    tree.pack(fill="both", expand=True)

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
    cours = item["values"][3]

    if messagebox.askyesno("Confirmation", f"Supprimer l'inscription de {prenom} dans le cours de {cours}?"):
        try:
            model.delete_row("Participants_has_cook_courses", {"id": insc_id})
            refresh_participants_courses()
            messagebox.showinfo("Succès", "inscription supprimée")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreeur de la suppression :{e}")



def add_inscription():
    """Ajoute une inscription à un cours."""

    traitement_participant = tk.StringVar()
    traitement_course = tk.StringVar()

    selected_participant = entry_participant.get()
    selected_course = entry_course.get

    traitement_participant.set(selected_participant)
    traitement_course.set(selected_course())

    participants_id = model.traduction_participants(traitement_participant.get())
    cook_courses_id = model.traduction_course(traitement_course.get())

    #logs de résultat

    print(participants_id)
    print(cook_courses_id)

    print(traitement_participant.get())
    print(traitement_course.get())

    try:
        participant_id = int(participants_id)
        course_id = int(cook_courses_id)
    except ValueError:
        messagebox.showerror("Erreur", "Echec opération")
        return

    course = model.get_course(course_id)

    # Vérifie la limite d'inscriptions
    currant_count = model.count_inscriptions(course_id)
    if course and currant_count >= course["max_place"]:
        messagebox.showwarning("Complet", "Ce cours est déjà complet")
        return

    success = model.insert_row("Participants_has_cook_courses", {
        "Participants_id": participant_id,
        "cook_courses_id": course_id
    })

    if success:
        messagebox.showinfo("Succès", "Inscription ajoutée.")
        entry_participant.delete(0, tk.END)
        entry_course.delete(0, tk.END)
        refresh_participants_courses()
    else:
        messagebox.showerror("Erreur", "Échec lors de l'ajout.")

def page_create_member ():
    subprocess.run(["Python", "create.py"])


# Fenêtre principale
root = tk.Tk()
root.title("Inscriptions aux Cours de Cuisine")
root.geometry("700x900")

btn_refresh = tk.Button(root, text="Rafraîchir", command=refresh_participants_courses, bg="blue", fg="white")
btn_refresh.pack(pady=5)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

form = tk.Frame(root, pady=10)
form.pack(fill="x")

liste_participants = model.contenu_deroulant_participants()
participants = [f"{row['first_name']}" for row in liste_participants]

tk.Label(form, text="Participant:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=2)
entry_participant = ttk.Combobox(form, width=20, font=("Arial", 12))
entry_participant["values"] = participants
entry_participant.current(0)
entry_participant.grid(row=0, column=1, padx=5, pady=5)

liste_course = model.contenu_deroulant_cours()
course = [row['name'] for row in liste_course]

print(course)

tk.Label(form, text="Cours:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=2)
entry_course = ttk.Combobox(form, width=20, font=("Arial", 12))
entry_course["values"] = course
entry_course.current(0)
entry_course.grid(row=1, column=1, padx=5, pady=5)

btn_add = tk.Button(form, text="Ajouter Inscription", command=add_inscription, bg="green", fg="white")
btn_add.grid(row=2, column=0, pady=5, padx=5)

btn_delete = tk.Button(form, text="Supprimer", command=lambda :delete_inscription(tree), bg="red", fg="white")
btn_delete.grid(row =2, column=1, pady=5, padx=5)

btn_page_create_member = tk.Button(form, text="Nouveau participant", command=page_create_member, bg="black", fg="white")
btn_page_create_member.grid(row=2, column=2, pady=5, padx=5)



refresh_participants_courses()
root.mainloop()