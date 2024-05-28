import tkinter as tk 
 
def main(): 
    root = tk.Tk() 
    root.title("Mi Proyecto Tkinter") 
    root.geometry("800x600") 
 
    lbl = tk.Label(root, text="¡Hola, Mundo!") 
    lbl.pack(pady=20) 
 
    root.mainloop() 
