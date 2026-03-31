import pandas as pd
import random

# Lê os dados do .csv
tabela = pd.read_csv("questionsdata.csv", sep=";")

# Embaralha a tabela e aloca uma variável índice que indica o número da linha
tabela = tabela.sample(frac=1)
indice = 0

# Inicia um loop para repetir as questões se a alternativa for certa ou errada
resposta = ()
while resposta != "SAIR":
    # Pega uma pergunta da lista embaralhada
    pergunta_aleatoria = tabela.iloc[indice]

    # Pega a pergunta e as alternativas
    pergunta = pergunta_aleatoria["Perguntas"]
    alternativas = {
        "A": pergunta_aleatoria["A"],
        "B": pergunta_aleatoria["B"],
        "C": pergunta_aleatoria["C"],
        "D": pergunta_aleatoria["D"]
        }
    # Inicia um loop para repetir a mesma pergunta enquanto a alternativa for inválida
    while resposta not in ["A", "B", "C", "D"]:
        print(f"{pergunta}\nA) {alternativas['A']}\nB) {alternativas['B']}\nC) {alternativas['C']}\nD) {alternativas['D']}")

        # Pega a resposta do usuário e confere se é a correta
        resposta_correta = pergunta_aleatoria["Resposta"].strip().upper()
        resposta = input('Digite a alternativa (Ou digite "Sair" para sair): ').upper()
        acertou = resposta == resposta_correta

        # Confere se as condições foram verdadeiras ou não e responde ao usuário     
        if acertou == True:
            print("Resposta correta!")
            break
        elif acertou == False and resposta in ["A", "B", "C", "D"]:
            print("Resposta incorreta.")
            break
        elif resposta == "SAIR":    
            break
        else:
            print("Alternativa Inválida")
    if resposta == "SAIR":
        print("Programa Encerrado")
        break
    # Adiciona 1 ao índice para passar para próxima linha da tabela, e reseta o valor da variável resposta
    indice += 1
    resposta = ()
    