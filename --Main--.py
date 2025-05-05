# Author : Jaruphong et Gaëtan

import tkinter as tk
from tkinter import messagebox
import model  # Import du fichier contenant les fonctions d'accès à la BD


def refresh_courses():
    """Rafraîchit l'affichage des courses."""
    for widget in frame.winfo_children():
        widget.destroy()  # Supprime tous les widgets pour recréer la liste

    courses = model.read_table("cook_courses")  # Récupère les cours depuis la BD

    if not courses:
        tk.Label(frame, text="Aucun cours trouvé.", font=("Arial", 12)).pack()
        return

    for course in courses:
        course_id = course["id"]
        course_name = course["name"]
        course_date = course["begin_time"]
        course_finish = course["finish_time"]
        course_price = course["price"]
        course_max = course["max_place"]
        course_last_inscription = course["last_inscription"]

        row_frame = tk.Frame(frame)
        row_frame.pack(fill="x", padx=5, pady=2)

        tk.Label(row_frame,
                 text=f"{course_id}: {course_name} - {course_date} - {course_finish} - Prix : {course_price} - Max de places : {course_max} - Dernier délais : {course_last_inscription}",
                 font=("Arial", 12)).pack(side="left", padx=5)

        btn_delete = tk.Button(row_frame, text="Delete", command=lambda cid=course_id: delete_course(cid), bg="red",
                               fg="white")
        btn_delete.pack(side="right", padx=5)


def delete_course(course_id):
    """Supprime un course après confirmation."""
    if messagebox.askyesno("Confirmation", f"Supprimer le cours ID {course_id} ?"):
        model.delete_row("cook_courses", {"id": course_id})
        refresh_courses()  # Met à jour l'affichage


def add_course():
    """Ajoute un concert à la base de données."""
    name = entry_name.get().strip()
    begin_time = entry_datetime.get().strip()

    if not name or not begin_time:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs !")
        return

    success = model.insert_row("cook_courses", {
        "name": name,
        "begin_time": begin_time,
        "price": 0.0,
        "max_place": 10,
        "places_id": 1,
        "teacher_id": 1,
    })
    if success:
        messagebox.showinfo("Succès", "Course ajouté avec succès !")
        entry_name.delete(0, tk.END)
        entry_datetime.delete(0, tk.END)
        refresh_courses()  # Met à jour l'affichage
    else:
        messagebox.showerror("Erreur", "Impossible d'ajouter le concert.")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion des cours ce cuisine")
root.geometry("950x500")

# Bouton de rafraîchissement
btn_refresh = tk.Button(root, text="Refresh", command=refresh_courses, bg="blue", fg="white")
btn_refresh.pack(pady=5)

# Frame pour afficher les concerts
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Formulaire d'ajout en bas
form_frame = tk.Frame(root, pady=10)
form_frame.pack(fill="x")

tk.Label(form_frame, text="Nom du cours:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=2)
entry_name = tk.Entry(form_frame, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=5, pady=2)

tk.Label(form_frame, text="Date/Heure:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=2)
entry_datetime = tk.Entry(form_frame, font=("Arial", 12))
entry_datetime.grid(row=1, column=1, padx=5, pady=2)

btn_add = tk.Button(form_frame, text="Ajouter", command=add_course, bg="green", fg="white")
btn_add.grid(row=2, columnspan=2, pady=5)

# Chargement initial des concerts
refresh_courses()

# Lancer l'application
root.mainloop()
