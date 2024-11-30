import tkinter as tk
from tkinter import messagebox

def validar_senhas():
    senha1 = entry_senha1.get()
    senha2 = entry_senha2.get()
    if senha1 == senha2:
        messagebox.showinfo("Sucesso", "As senhas estão corretas!")
    else:
        messagebox.showerror("Erro", "As senhas estão incorretas!")

def toggle_password(entry, btn):
    if entry.cget('show') == '':
        entry.config(show='*')
        btn.config(text="👁️")
    else:
        entry.config(show='')
        btn.config(text="🙈")

# Configuração da janela principal
root = tk.Tk()
root.title("Validação de Senha")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

# Estilo geral
font_style = ("Arial", 12)
bg_color = "#f0f8ff"
btn_color = "#4682b4"
btn_fg = "#ffffff"

# Rótulo principal
label_titulo = tk.Label(root, text="Validador de Senha", font=("Arial", 16, "bold"), bg=bg_color, fg="#2f4f4f")
label_titulo.pack(pady=10)

# Campo de senha 1
frame_senha1 = tk.Frame(root, bg=bg_color)
frame_senha1.pack(pady=10)
label_senha1 = tk.Label(frame_senha1, text="Digite a senha:", font=font_style, bg=bg_color)
label_senha1.pack(side=tk.LEFT, padx=5)
entry_senha1 = tk.Entry(frame_senha1, font=font_style, show='*', width=20)
entry_senha1.pack(side=tk.LEFT)
btn_toggle1 = tk.Button(frame_senha1, text="👁️", font=("Arial", 10), command=lambda: toggle_password(entry_senha1, btn_toggle1))
btn_toggle1.pack(side=tk.LEFT, padx=5)

# Campo de senha 2
frame_senha2 = tk.Frame(root, bg=bg_color)
frame_senha2.pack(pady=10)
label_senha2 = tk.Label(frame_senha2, text="Confirme a senha:", font=font_style, bg=bg_color)
label_senha2.pack(side=tk.LEFT, padx=5)
entry_senha2 = tk.Entry(frame_senha2, font=font_style, show='*', width=20)
entry_senha2.pack(side=tk.LEFT)
btn_toggle2 = tk.Button(frame_senha2, text="👁️", font=("Arial", 10), command=lambda: toggle_password(entry_senha2, btn_toggle2))
btn_toggle2.pack(side=tk.LEFT, padx=5)

# Botão de validação
btn_validar = tk.Button(root, text="Confirmar", font=("Arial", 14, "bold"), bg=btn_color, fg=btn_fg, command=validar_senhas)
btn_validar.pack(pady=20)

# Rodar o programa
root.mainloop()
