import tkinter as tk
from tkinter import PhotoImage, messagebox
from PIL import Image, ImageTk
import os

verificar = 0
tentativas = 0
sacar = 0
saldo_atual = 50.20  # saldo inicial

# Função para exibir janelas personalizadas com texto grande
def mostrar_mensagem_grande(titulo, mensagem, cor="black"):
    janela_mensagem = tk.Toplevel(janela)
    janela_mensagem.title(titulo)
    janela_mensagem.geometry("400x200")
    janela_mensagem.resizable(False, False)

    label = tk.Label(janela_mensagem, text=mensagem, font=("Helvetica", 18), fg=cor, wraplength=380)
    label.pack(pady=30)

    botao_fechar = tk.Button(janela_mensagem, text="Fechar", command=janela_mensagem.destroy, font=("Helvetica", 12))
    botao_fechar.pack(pady=10)

# Verifica saldo atual
def verificar_saldo():
    mostrar_mensagem_grande("💰 Extrato", f"Seu saldo atual é: {saldo_atual:.2f}$", cor="green")

# Função de saque
def sacar_saque():
    global saldo_atual
    valor = entrada_sacar_saldo.get()

    if not valor.replace('.', '', 1).isdigit():
        mostrar_mensagem_grande("Erro", "Digite um valor válido para saque.", cor="red")
        return

    valor = float(valor)
    if valor > saldo_atual:
        mostrar_mensagem_grande("Saldo Insuficiente", f"💸 Seu limite é {saldo_atual:.2f}$", cor="blue")
    else:
        saldo_atual -= valor
        mostrar_mensagem_grande("Saque Realizado", f"Saque de {valor:.2f}$ efetuado com sucesso!", cor="green")

# Função de depósito
def depositar_valor():
    global saldo_atual
    valor = entrada_deposito.get()

    if not valor.replace('.', '', 1).isdigit():
        mostrar_mensagem_grande("Erro", "Digite um valor válido para depósito.", cor="red")
        return

    valor = float(valor)
    saldo_atual += valor
    mostrar_mensagem_grande("Depósito Realizado", f"Depósito de {valor:.2f}$ efetuado com sucesso!", cor="green")

# Função de sair com confirmação
def sair_aplicacao():
    resposta = messagebox.askyesno("Sair", "Deseja realmente sair do aplicativo?")
    if resposta:
        janela.destroy()

# Janela principal
janela = tk.Tk()
janela.title("Banco - IM OUT OF MONEY")
janela.geometry("1000x600")
janela.resizable(False, False)

# Imagem de fundo
caminho_imagem = "C:/Users/919153/Desktop/PYTHON/TKINTER/bank.png"
if os.path.exists(caminho_imagem):
    imagem_original = Image.open(caminho_imagem)
    try:
        resample = Image.Resampling.LANCZOS
    except AttributeError:
        resample = Image.ANTIALIAS
    imagem_redimensionada = imagem_original.resize((1000, 600), resample)
    imagem_fundo = ImageTk.PhotoImage(imagem_redimensionada)
    fundo_label = tk.Label(janela, image=imagem_fundo)
    fundo_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    tk.Label(janela, text="[Imagem não encontrada]", fg="red").pack()

# Título



# Entrada e botão de saldo
botao_saldo = tk.Button(janela, text="Verificar Saldo", command=verificar_saldo, font=("Helvetica", 12))
botao_saldo.place(relx=0.5, rely=0.30, anchor="center")

# Entrada e botão de saque
entrada_sacar_saldo = tk.Entry(janela, font=("Helvetica", 12), justify='center')
entrada_sacar_saldo.place(relx=0.5, rely=0.40, anchor="center")

botao_sacar_saldo = tk.Button(janela, text="Sacar Saldo", command=sacar_saque, font=("Helvetica", 12))
botao_sacar_saldo.place(relx=0.5, rely=0.45, anchor="center")

# Entrada e botão de depósito
entrada_deposito = tk.Entry(janela, font=("Helvetica", 12), justify='center')
entrada_deposito.place(relx=0.5, rely=0.55, anchor="center")

botao_depositar = tk.Button(janela, text="Depositar", command=depositar_valor, font=("Helvetica", 12))
botao_depositar.place(relx=0.5, rely=0.60, anchor="center")

# Botão SAIR (antigo Verificar Palpite)
botao_sair = tk.Button(janela, text="Sair", command=sair_aplicacao, font=("Helvetica", 12), bg="red", fg="white")
botao_sair.place(relx=0.49500, rely=0.75, anchor="center")

# Inicia a interface
janela.mainloop()
