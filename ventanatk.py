import tkinter as tk

window = tk.Tk()
window.title('Mi primera ventana')

# Crear un campo de entrada
entra_texto = tk.Entry(window, font=('calibri', 10))
entra_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()
