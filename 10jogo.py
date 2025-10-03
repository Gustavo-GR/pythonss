import tkinter as tk  # Importa a biblioteca tkinter e a renomeia como tk para facilitar o uso
from tkinter import messagebox  # Importa o módulo messagebox do tkinter para exibir caixas de mensagem
from tkinter import PhotoImage  # Importa a classe PhotoImage do tkinter para exibir imagens
import random  # Importa o módulo random para gerar números aleatórios
import os  # Importa o módulo os para interagir com o sistema operacional

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0  # Inicializa o contador de tentativas

def verificar_palpite():
    global tentativas  # Permite que a função modifique a variável global tentativas
    try:
        palpite = int(entrada_palpite.get())  # Obtém o palpite do usuário e converte para inteiro
        tentativas += 1  # Incrementa o contador de tentativas

        if palpite < numero_secreto:
            resultado_label.config(text="Muito baixo! Tente novamente.", fg="blue")  # Atualiza o rótulo de resultado
        elif palpite > numero_secreto:
            resultado_label.config(text="Muito alto! Tente novamente.", fg="red")  # Atualiza o rótulo de resultado
        else:
            messagebox.showinfo("Parabéns!", f"Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            janela.quit()  # Fecha a janela do jogo
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")  # Exibe mensagem de erro se o palpite não for um número válido

# Janela principal
janela = tk.Tk()  # Cria a janela principal do jogo
janela.title("Jogo de Adivinhação")  # Define o título da janela
janela.geometry("700x1000")  # Define o tamanho da janela

# Caminho absoluto para a imagem
caminho_imagem = "C:/Users/919153/Desktop/PYTHON/TKINTER/numeros.png"

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
