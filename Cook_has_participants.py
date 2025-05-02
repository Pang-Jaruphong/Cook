import tkinter as tk
from tkinter import messagebox
import model  # module d'accès à la BD


def refresh_participants_courses():
    """Affiche les inscriptions (participants à des cours)."""
    for widget in frame.winfo_children():
        widget.destroy()

    inscriptions = model.get_participants_courses()

    if not inscriptions:
        tk.Label(frame, text="Aucune inscription trouvée.", font=("Arial", 12)).pack()
        return

    for insc in inscriptions:
        insc_id = insc["id"]
        fullname = f"{insc['first_name']} {insc['last_name']}"
        course = insc["course_name"]

        row = tk.Frame(frame)
        row.pack(fill="x", padx=5, pady=2)

        label_text = f"Inscription #{insc_id} - {fullname} est inscrit au cours {course}."
        tk.Label(row, text=label_text, font=("Arial", 12)).pack(side="left", padx=5)

        btn = tk.Button(row, text="Supprimer", command=lambda iid=insc_id: delete_inscription(iid), bg="red",
                        fg="white")
        btn.pack(side="right")

def delete_inscription(insc_id):
    """Supprime une inscription."""
    if messagebox.askyesno("Confirmation", f"Supprimer l'inscription ID {insc_id} ?"):
        model.delete_row("Participants_has_cook_courses", {"id": insc_id})
        refresh_participants_courses()


def add_inscription():
    """Ajoute une inscription à un cours."""
    try:
        participant_id = int(entry_participant.get().strip())
        course_id = int(entry_course.get().strip())
    except ValueError:
        messagebox.showerror("Erreur", "ID invalide (doivent être numériques)")
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
        messagebox.showerror("Erreur", "Échec lors de l'ajout. Vérifiez les ID (existants dans la BD).")


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

tk.Label(form, text="ID Participant:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=2)
entry_participant = tk.Entry(form, font=("Arial", 12))
entry_participant.grid(row=0, column=1, padx=5, pady=2)

tk.Label(form, text="ID Cours:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=2)
entry_course = tk.Entry(form, font=("Arial", 12))
entry_course.grid(row=1, column=1, padx=5, pady=2)

btn_add = tk.Button(form, text="Ajouter Inscription", command=add_inscription, bg="green", fg="white")
btn_add.grid(row=2, columnspan=2, pady=5)

refresh_participants_courses()
root.mainloop()