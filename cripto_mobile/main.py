import tkinter as tk
from tkinter import messagebox
import threading
from api import obter_cotacao_cripto

def mostrar_cotacao_com_carregamento():
    """Função para exibir a cotação com feedback de carregamento"""
    # Exibe a tela de carregamento
    carregando_label.config(text="Carregando...", fg="#038C65")
    
    def buscar():
        cripto = cripto_entry.get().lower()
        moeda = moeda_entry.get().lower()
        
        # Verifica se as entradas não estão vazias
        if cripto == "" or moeda == "":
            messagebox.showwarning("Entrada inválida", "Por favor, preencha os campos de criptomoeda e moeda.")
            carregando_label.config(text="")
            return
        
        # Tenta obter a cotação
        preco = obter_cotacao_cripto(cripto, moeda)

        # Verifica se a resposta é uma cotação válida (float)
        if isinstance(preco, float):
            # Exibe a cotação formatada corretamente com a mensagem completa
            resultado_label.config(text=f"A cotação para a {cripto.upper()} em {moeda.upper()} é: {preco:.2f}")
            resultado_label.config(bg="#02735E", fg="#011526", font=("Helvetica", 14, "bold"))
        else:
            # Exibe a mensagem de erro caso a resposta seja um código de erro numérico
            resultado_label.config(text=f"Erro na consulta. Código de erro: {preco}")
            resultado_label.config(bg="#025959", fg="#011526", font=("Helvetica", 14, "bold"))
            print(f"Erro na consulta: {preco}")  # Imprime no terminal a resposta da API
        
        # Limpa a mensagem de carregamento
        carregando_label.config(text="")

    # Cria uma nova thread para rodar a função de busca sem bloquear a interface
    threading.Thread(target=buscar).start()

def limpar_campos():
    """Limpa os campos de entrada e o campo de resultado"""
    cripto_entry.delete(0, tk.END)
    moeda_entry.delete(0, tk.END)
    resultado_label.config(text="")
    resultado_label.config(bg="#f4f4f9", fg="#011526", font=("Helvetica", 14))

def sair_aplicacao():
    """Fecha a aplicação com uma confirmação"""
    resposta = messagebox.askyesno("Confirmar saída", "Você tem certeza que deseja sair?")
    if resposta:
        root.quit()

# Configuração da janela principal
root = tk.Tk()
root.title("Consulta de Cotação de Criptomoedas")
root.geometry("600x600")  # Aumenta a altura da janela para mais conforto
root.config(bg="#011526")  # Cor de fundo mais escura

# Layout da interface
frame = tk.Frame(root, bg="#011526")
frame.pack(pady=30, padx=20)

# Título
titulo_label = tk.Label(frame, text="Consulta de Criptomoeda", font=("Helvetica", 20, "bold"), bg="#011526", fg="#038C65")
titulo_label.grid(row=0, column=0, columnspan=2, pady=20)

# Rótulos
cripto_label = tk.Label(frame, text="Criptomoeda (ex: bitcoin):", font=("Helvetica", 12), bg="#011526", fg="#038C65")
cripto_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

moeda_label = tk.Label(frame, text="Moeda (ex: brl, usd):", font=("Helvetica", 12), bg="#011526", fg="#038C65")
moeda_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Entradas de texto com fundo harmonizado
cripto_entry = tk.Entry(frame, width=25, font=("Helvetica", 12), relief="solid", bd=2, fg="#011526", bg="#60BF81", insertbackground="#011526")  # Cor de fundo mais clara
cripto_entry.grid(row=1, column=1, padx=10, pady=10)

moeda_entry = tk.Entry(frame, width=25, font=("Helvetica", 12), relief="solid", bd=2, fg="#011526", bg="#60BF81", insertbackground="#011526")  # Cor de fundo mais clara
moeda_entry.grid(row=2, column=1, padx=10, pady=10)

# Botões de ações
buscar_button = tk.Button(frame, text="Buscar Cotação", font=("Helvetica", 12), bg="#025959", fg="white", command=mostrar_cotacao_com_carregamento, width=20, height=2, relief="raised")
buscar_button.grid(row=3, column=0, columnspan=2, pady=15)

limpar_button = tk.Button(frame, text="Limpar", font=("Helvetica", 12), bg="#02735E", fg="white", command=limpar_campos, width=20, height=2, relief="raised")
limpar_button.grid(row=4, column=0, columnspan=2, pady=10)

sair_button = tk.Button(frame, text="Sair", font=("Helvetica", 12), bg="#038C65", fg="white", command=sair_aplicacao, width=20, height=2, relief="raised")
sair_button.grid(row=5, column=0, columnspan=2, pady=15)

# Label de carregamento
carregando_label = tk.Label(root, text="", font=("Helvetica", 12), fg="#038C65", bg="#011526")
carregando_label.pack(pady=10)

# Caixa de resultado
resultado_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f4f4f9", fg="#011526", width=40, height=4, relief="solid", bd=2, anchor="w", justify="left")
resultado_label.pack(pady=15)

# Inicia o loop da interface gráfica
root.mainloop()
