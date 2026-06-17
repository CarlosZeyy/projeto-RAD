import tkinter as tk
from tkinter import messagebox
import connectDB as db
from connectDB import *

def add_user():
    name = entry_name.get()

    if name.strip():
        conn = db.connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

        entry_name.delete(0, tk.END)
        update_list()
    else:
        messagebox.showwarning("Aviso", "Por favor, digite um nome!")
    
def update_list():
    listbox_users.delete(0, tk.END)

    conn = db.connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM users")

    for row in cursor.fetchall():
        listbox_users.insert(tk.END, row[0])
    
    conn.close()

# Styles

# Paleta de Cores (Tema Dark)
BG_COLOR = "#1a1b26"        
ENTRY_BG = "#24283b"        
FG_COLOR = "#c0caf5"        
BTN_COLOR = "#7aa2f7"       
BTN_ACTIVE = "#8db3f8"      
BORDER_COLOR = "#414868"    

# Fonts
FONT_DEFAULT = ("Segoe UI", 10)
FONT_TITLE = ("Segoe UI", 12, "bold")

window = tk.Tk()
window.title("Projeto Acadêmico - Cadastro")
window.geometry("1280x720")
window.configure(bg=BG_COLOR)

connection()

#Title
tk.Label(
    window, 
    text="Nome do usuário:", 
    bg=BG_COLOR, 
    fg=FG_COLOR, 
    font=FONT_TITLE
).pack(pady=(20, 5))

# Entry (input)
entry_name = tk.Entry(
    window, 
    width=35,
    bg=ENTRY_BG,
    fg=FG_COLOR,
    font=FONT_DEFAULT,
    insertbackground=FG_COLOR, # Cor do cursor piscando
    relief="flat",             # Remove o efeito 3D antigo
    highlightthickness=1,      # Espessura da borda customizada
    highlightbackground=BORDER_COLOR,
    highlightcolor=BTN_COLOR   # Cor da borda quando selecionado
)
entry_name.pack(pady=5, ipady=5) # ipady dá uma "engordada" interna no campo

# Button
tk.Button(
    window, 
    text="Adicionar ao Banco", 
    command=add_user,
    bg=BTN_COLOR,
    fg=BG_COLOR,
    font=("Segoe UI", 10, "bold"),
    activebackground=BTN_ACTIVE,
    activeforeground=BG_COLOR,
    relief="flat",
    cursor="hand2"              
).pack(pady=15, ipadx=10, ipady=5)

# Sub-title
tk.Label(
    window, 
    text="Usuários cadastrados:", 
    bg=BG_COLOR, 
    fg=FG_COLOR, 
    font=FONT_TITLE
).pack(pady=(15, 5))

# Listbox
listbox_users = tk.Listbox(
    window, 
    width=40, 
    height=10,
    bg=ENTRY_BG,
    fg=FG_COLOR,
    font=FONT_DEFAULT,
    relief="flat",
    highlightthickness=1,
    highlightbackground=BORDER_COLOR,
    selectbackground=BTN_COLOR,   # Cor ao selecionar um item na lista
    selectforeground=BG_COLOR
)
listbox_users.pack(pady=5)

update_list()

window.mainloop()