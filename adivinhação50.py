import tkinter as tk  
from tkinter import messagebox  
from tkinter import PhotoImage 
import random
import os  

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0  # Inicializa o contador de tentativas

def verificar_palpite():
    global tentativas  
    try:
        palpite = int(entrada_palpite.get())  
        tentativas += 1  

        if palpite < numero_secreto:
            resultado_label.config(text="Muito baixo! Tente novamente.", fg="blue")  
        elif palpite > numero_secreto:
            resultado_label.config(text="Muito alto! Tente novamente.", fg="red")  
        else:
            messagebox.showinfo("Parabéns!", f"Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            janela.quit()  
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")  

# Janela principal
janela = tk.Tk()  # Cria a janela principal do jogo
janela.title("Jogo de Adivinhação")  # Define o título da janela
janela.geometry("1250x1000")  # Define o tamanho da janela

# Caminho absoluto para a imagem
caminho_imagem = "C:/Users/919153/Desktop/PYTHON/TKINTER/123.png"

# Verifica se a imagem existe
if os.path.exists(caminho_imagem):
    tente_novamente_img = PhotoImage(file=caminho_imagem)  # Carrega a imagem
    img_label = tk.Label(janela, image=tente_novamente_img)  # Cria um rótulo para exibir a imagem
    img_label.image = tente_novamente_img  # Manter referência para evitar descarte da imagem
    img_label.pack(pady=10)  # Adiciona o rótulo à janela
else:
    tk.Label(janela, text="[Imagem não encontrada]", fg="red").pack(pady=10)  # Exibe mensagem se a imagem não for encontrada

# Elementos da interface gráfica
tk.Label(janela, text="Bem-vindo ao jogo de adivinhação!\nTente adivinhar o número entre 1 e 100.",
         fg="green", font=("Helvetica", 12)).pack(pady=10)  # Adiciona um rótulo com instruções

entrada_palpite = tk.Entry(janela)  # Cria uma caixa de entrada para o palpite do usuário
entrada_palpite.pack(pady=5)  # Adiciona a caixa de entrada à janela

botao_verificar = tk.Button(janela, text="Verificar Palpite", command=verificar_palpite)  # Cria um botão para verificar o palpite
botao_verificar.pack(pady=10)  # Adiciona o botão à janela

resultado_label = tk.Label(janela, text="", font=("Helvetica", 10))  # Cria um rótulo para exibir o resultado do palpite
resultado_label.pack(pady=10)  # Adiciona o rótulo à janela

# Iniciar loop principal da interface gráfica
janela.mainloop()  # Inicia o loop principal da interface gráfica, que mantém a janela aberta e processa eventos
