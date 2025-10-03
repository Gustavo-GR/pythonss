import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random
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

# Função de palpite
def verificar_palpite():
    global tentativas
    palpite = entrada_palpite.get()

    if not palpite.isdigit():
        mostrar_mensagem_grande("Erro", "Digite um número válido entre 1 e 100", cor="red")
        return

    palpite = int(palpite)
    tentativas += 1

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

# Janela principal
janela = tk.Tk()
janela.title("Banco - IM OUT OF MONEY")
janela.geometry("1000x600")
janela.resizable(False, False)


# Imagem de fundo
caminho_imagem = "C:/Users/919153/Desktop/PYTHON/TKINTER/banco.jpg"
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
titulo_label = tk.Label(janela, text="BEM-VINDO AO BANCO IM OUT OF MONEY",
                        fg="black", font=("Helvetica", 20), bg="#ffffff")
titulo_label.place(relx=0.5, rely=0.10, anchor="center")

# Entrada e botão de palpite
entrada_palpite = tk.Entry(janela, font=("Helvetica", 12), justify='center')
entrada_palpite.place(relx=0.5, rely=0.25, anchor="center")

botao_verificar = tk.Button(janela, text="Verificar Palpite", command=verificar_palpite, font=("Helvetica", 12))
botao_verificar.place(relx=0.5, rely=0.30, anchor="center")

# Entrada e botão de saldo
entrada_saldo = tk.Entry(janela, font=("Helvetica", 12), justify='center')  # não usada mais, mas deixada para manter estrutura
entrada_saldo.place_forget()

botao_saldo = tk.Button(janela, text="Verificar Saldo", command=verificar_saldo, font=("Helvetica", 12))
botao_saldo.place(relx=0.5, rely=0.40, anchor="center")

# Entrada e botão de saque
entrada_sacar_saldo = tk.Entry(janela, font=("Helvetica", 12), justify='center')
entrada_sacar_saldo.place(relx=0.5, rely=0.50, anchor="center")

botao_sacar_saldo = tk.Button(janela, text="Sacar Saldo", command=sacar_saque, font=("Helvetica", 12))
botao_sacar_saldo.place(relx=0.5, rely=0.55, anchor="center")

# Entrada e botão de depósito
entrada_deposito = tk.Entry(janela, font=("Helvetica", 12), justify='center')
entrada_deposito.place(relx=0.5, rely=0.65, anchor="center")

botao_depositar = tk.Button(janela, text="Depositar", command=depositar_valor, font=("Helvetica", 12))
botao_depositar.place(relx=0.5, rely=0.70, anchor="center")

# Inicia a interface
janela.mainloop()
