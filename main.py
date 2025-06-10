# Connection à une BD
# Il faut avoir installé mysqlconnector (pip install mysql-connector-python)
# Author : Jaruphong et Gaëtan
# Version 1.0 Date : 10.06.2025

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importer Themed Tkinter, widgets pour améliorer l'affiche
import model  # Import du fichier contenant les fonctions d'accès à la BD

tree = None


def refresh_courses():
    """Rafraîchit l'affichage des courses."""
    global tree
    for widget in frame.winfo_children():
        widget.destroy()  # Supprime tous les widgets pour recréer la liste

    courses = model.read_table("cook_courses")  # Récupère les cours depuis la BD

    if not courses:
        tk.Label(frame, text="Aucun cours trouvé.", font=("Arial", 12)).pack()
        tree = None
        return

    columns = ("id", "name", "begin_time", "finish_time", "price", "max_place", "last_inscription")
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Définir les titres des colonnes
    tree.heading("id", text="ID")
    tree.heading("name", text="Nom")
    tree.heading("begin_time", text="Commencer")
    tree.heading("finish_time", text="Finir")
    tree.heading("price", text="Prix")
    tree.heading("max_place", text="Max de places")
    tree.heading("last_inscription", text="Dernier délais")

    # Ajuster la largeur
    for col in columns:
        tree.column(col, width=100)

    # Remplir le tabeau
    for course in courses:
        # Ajouter une ligne dans le tableau Treeview,
        # "" ajouter l'élément à la racine (pas dans un groupe hiérarchique)
        # "end" ajouter à la fin de la liste actuelle
        # values=(...), les données de chaque colonne
        tree.insert("", "end", values=(
            course["id"],
            course["name"],
            course["begin_time"],
            course["finish_time"],
            course["price"],
            course["max_place"],
            course["last_inscription"],
        ))

    # Affiche ce tableau, utilise tout l'espace
    tree.pack(fill="both", expand=True)


def delete_course(tree):
    """Supprime un cours après confirmation."""
    if not tree:
        messagebox.showerror("Erreur", "Aucune liste affichée.")
        return

    selection = tree.selection()

    if not selection:
        messagebox.showwarning("Aucun élément sélectionné", "Veuillez sélectionner une inscription à supprimer.")
        return

    # On suppose que l'ID est dans la première colonne
    item = tree.item(selection[0])
    course_id = item["values"][1]
    if messagebox.askyesno("Confirmation", f"Supprimer le cours : {course_id} ?"):
        try:
            model.delete_row("cook_courses", {"id": course_id})
            refresh_courses()  # Met à jour l'affichage
            messagebox.showinfo("Succès", "inscription supprimée")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreeur de la suppression :{e}")


def add_course():
    """Ajoute un concert à la base de données."""
    name = entry_name.get().strip()
    begin_time = entry_datetime.get().strip()
    raw_time = entry_finish_time.get().strip()
    price = entry_price.get().strip()
    max_place = entry_max_place.get().strip()
    last_inscription = entry_last_inscription.get().strip()

    try:
        # Conversion vers un format TIME MySQL (HH:MM:SS) et le prix
        price = float(entry_price.get().replace(",", ".").strip())
        # Formatage de l'heure de fin en HH:MM:00 (5 caratères)
        if len(raw_time) == 5:
            finish_time = raw_time + ":00"  # ex. '18:30:00'
        else:
            finish_time = raw_time  # au cas où déjà sous forme HH:MM:SS
    except ValueError:
        messagebox.showerror("Erreur", "Prix et Heure de fin invalide (format attendu HH:MM)")
        return

    if not name or not begin_time or not last_inscription or not raw_time or not price or not finish_time:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs !")
        return

    success = model.insert_row("cook_courses", {
        "name": name,
        "begin_time": begin_time,
        "finish_time": finish_time,
        "price": price,
        "max_place": max_place,
        "last_inscription": last_inscription,
        "places_id": 1,
        "teachers_id": 1,
    })
    if success:
        messagebox.showinfo("Succès", "Le cours ajouté avec succès !")
        entry_name.delete(0, tk.END)
        entry_datetime.delete(0, tk.END)
        entry_finish_time.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_max_place.delete(0, tk.END)
        entry_last_inscription.delete(0, tk.END)
        refresh_courses()  # Met à jour l'affichage
    else:
        messagebox.showerror("Erreur", "Impossible d'ajouter le cours.")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion des cours de cuisine")
root.geometry("950x450")

# Bouton de rafraîchissement
btn_refresh = tk.Button(root, text="Refresh", command=refresh_courses, bg="blue", fg="white")
btn_refresh.pack(pady=5)

# Frame pour afficher les courses
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Formulaire d'ajout en bas
form_frame = tk.Frame(root, pady=10)
form_frame.pack(fill="x")

tk.Label(form_frame, text="Nom du cours:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=2)
entry_name = tk.Entry(form_frame, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=5, pady=2)

tk.Label(form_frame, text="Date/Heure:", font=("Arial", 12)).grid(row=0, column=2, padx=5, pady=2)
entry_datetime = tk.Entry(form_frame, font=("Arial", 12))
entry_datetime.grid(row=0, column=3, padx=5, pady=2)

tk.Label(form_frame, text="Fin:", font=("Arial", 12)).grid(row=0, column=4, padx=5, pady=2)
entry_finish_time = tk.Entry(form_frame, font=("Arial", 12))
entry_finish_time.grid(row=0, column=5, padx=5, pady=2)

tk.Label(form_frame, text="Prix:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=2)
entry_price = tk.Entry(form_frame, font=("Arial", 12))
entry_price.grid(row=1, column=1, padx=5, pady=2)

tk.Label(form_frame, text="Max de place:", font=("Arial", 12)).grid(row=1, column=2, padx=5, pady=2)
entry_max_place = tk.Entry(form_frame, font=("Arial", 12))
entry_max_place.grid(row=1, column=3, padx=5, pady=2)

tk.Label(form_frame, text="Dernier délais:", font=("Arial", 12)).grid(row=1, column=4, padx=5, pady=2)
entry_last_inscription = tk.Entry(form_frame, font=("Arial", 12))
entry_last_inscription.grid(row=1, column=5, padx=5, pady=2)

btn_add = tk.Button(form_frame, text="Ajouter", command=add_course, bg="green", fg="white")
btn_add.grid(row=2, columnspan=5, pady=5, padx=5)

btn_delete = tk.Button(form_frame, text="Supprimer", command=lambda: delete_course(tree), bg="red", fg="white")
btn_delete.grid(row=2, columnspan=8, pady=5, padx=5)

# Chargement initial des courses
refresh_courses()

# Lancer l'application
root.mainloop()