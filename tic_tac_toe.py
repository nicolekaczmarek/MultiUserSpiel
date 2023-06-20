import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("spieler.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Spieler (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Punktestand INTEGER)")

window = tk.Tk()
window.title("Spiel")
window.geometry("300x200")


label_x = tk.Label(window, text="Spieler X:")
label_x.pack()
entry_x = tk.Entry(window)
entry_x.pack()

label_o = tk.Label(window, text="Spieler O:")
label_o.pack()
entry_o = tk.Entry(window)
entry_o.pack()


def start_game():
    player_x = entry_x.get()
    player_o = entry_o.get()

    if not player_x or not player_o:
        messagebox.showwarning("Fehler", "Bitte geben Sie die Namen beider Spieler ein.")
        return

    cursor.execute("INSERT INTO Spieler (Name, Punktestand) VALUES (?, ?)", (player_x, 0))
    cursor.execute("INSERT INTO Spieler (Name, Punktestand) VALUES (?, ?)", (player_o, 0))
    conn.commit()

    messagebox.showinfo("Spiel gestartet", f"Spieler X: {player_x}\nSpieler O: {player_o}")
    window.destroy()


start_button = tk.Button(window, text="Spiel starten", command=start_game)
start_button.pack()
def start_tournament():
    pass
tournament_button = tk.Button(window, text="Turnier starten", command=start_tournament)
tournament_button.pack()

window.mainloop()