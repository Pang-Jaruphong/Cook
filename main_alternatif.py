#importations

from tkinter import *
from tkinter import messagebox
import tkinter.font
import tkinter as tk
from tkinter import ttk
import mysql.connector

#Connexion à la base de donnée, sera remplacé par l'appel d'un autre fichier

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cookingclasses")

curseur = conn.cursor()

def inscription():
    pass

inter = Tk()
inter.geometry("800x900")
inter.title('Cours de cuisine')
inter.configure(bg="#FFFFFF")

lbl_titre = Label(inter,text="Cours culinaires culturels", height=2, font=("Helvetica", 48), bg="#FFFFFF", fg="#000000")
lbl_titre.pack()

#Création des tableaux

#Récupération des données, classée par Treeview (l'utilisation de ce dernier est une proposition fonctionnelle de ChatGPT)

colonnes_cours = ("Cours", "Lieu", "Date", "Durée", "Prix", "Professeur")
tableau_cours = ttk.Treeview(inter, columns=colonnes_cours, show="headings")

curseur.execute("SELECT name, begin_time, finish_time, price, max_place FROM cook_courses")

cours = curseur.fetchall()

#Fabrication et affichage du tableau

for col in colonnes_cours:
    tableau_cours.heading(col, text=col)
    tableau_cours.column(col, width=100)

for ligne in cours:
    tableau_cours.insert("", tk.END, values=ligne)

tableau_cours.pack(expand=True, fill="both")

lbl_participant = Label(inter,text="Participants", height=2, font=("Helvetica", 20), bg="#FFFFFF", fg="#000000")
lbl_participant.pack()

#Le tableau des participants suit le même processus que pour les cours

#curseur.execute("SELECT first_name, last_name FROM participants JOIN cook_courses ON participants_has_cook_courses.cook_courses_id = cook_courses.id")
curseur.execute("""SELECT
                participants.first_name AS participant,
                participants.last_name AS participant,
                cook_courses.name AS cours
                FROM participants_has_cook_courses
                INNER JOIN participants ON participants_has_cook_courses.participants_id = participants.id
                INNER JOIN cook_courses ON participants_has_cook_courses.cook_courses_id = cook_courses.id""")

participants = curseur.fetchall()

colonnes_participants = ("Prenom", "nom", "cours")
tableau_participants = ttk.Treeview(inter, columns=colonnes_participants, show="headings")

tableau_participants.pack(expand=True, fill="both")

for col in colonnes_participants:
    tableau_participants.heading(col, text=col)
    tableau_participants.column(col, width=100)

for ligne in participants:
    tableau_participants.insert("", tk.END, values=ligne)

#Bouton d'inscription (qui fonctionnera dans une future version)

inscription = tk.Button(inter, text="Inscription", command=inscription, bg="#FFFFFF", fg="#000000", font=("Helvetica", 14))
inscription.pack()

inter.mainloop()