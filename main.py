import pandas as pd
import unidecode

# Lê os dados do .csv de acordo com a dificuldade
diff = unidecode.unidecode(input("Digite o nível de dificuldade (Fácil, médio, difícil, misturado): ")).lower()
tabela = pd.read_csv("questionsdata_completo.csv", sep=";")
if diff == "facil":
    tabela = tabela[tabela["Nivel"] == "Facil"]
elif diff == "medio":
    tabela = tabela[tabela["Nivel"] == "Medio"]
elif diff == "dificil":
    tabela = tabela[tabela["Nivel"] == "Dificil"]
elif diff == "misturado":
    tabela = pd.read_csv("questionsdata_completo.csv", sep=";")

# Embaralha a tabela e aloca uma variável índice que indica o número da linha, pega o número total de linhas
tabela = tabela.sample(frac=1)
indice = 0
pontos = 0
total_linhas = len(tabela)

# Inicia um loop para repetir as questões se a alternativa for certa ou errada
resposta = ()
while resposta != "SAIR":
    # Para se acabarem as perguntas
    if indice >= total_linhas:
        print("Você completou as questões!")
        break
    # Pega uma pergunta da lista embaralhada
    pergunta_aleatoria = tabela.iloc[indice]

    # Pega a pergunta, as alternativas, e a dificuldade
    pergunta = pergunta_aleatoria["Perguntas"]
    alternativas = {
        "A": pergunta_aleatoria["A"],
        "B": pergunta_aleatoria["B"],
        "C": pergunta_aleatoria["C"],
        "D": pergunta_aleatoria["D"]
        }
    dificuldade = pergunta_aleatoria["Nivel"]
    # Inicia um loop para repetir a mesma pergunta enquanto a alternativa for inválida
    while resposta not in ["A", "B", "C", "D"]:
        print(f"{pergunta}\nA) {alternativas['A']}\nB) {alternativas['B']}\nC) {alternativas['C']}\nD) {alternativas['D']}\n Nível: {dificuldade}")

        # Pega a resposta do usuário e confere se é a correta
        resposta_correta = pergunta_aleatoria["Resposta"].strip().upper()
        resposta = input('Digite a alternativa (Ou digite "Sair" para sair): ').upper()
        acertou = resposta == resposta_correta

        # Confere se as condições foram verdadeiras ou não e responde ao usuário     
        if acertou == True:
            pontos +=1
            print("-"*30)
            print(f"Resposta correta! Você está com {pontos} pontos!")
            print("-"*30)
            break
        elif acertou == False and resposta in ["A", "B", "C", "D"]:
            print("-"*30)
            print("Resposta incorreta.")
            print("-"*30)
            break
        elif resposta == "SAIR":    
            break
        else:
            print("-"*30)
            print("Alternativa Inválida")
            print("-"*30)
    if resposta == "SAIR":
        print("-"*30)
        print("Programa Encerrado")
        print("-"*30)
        break
    # Adiciona 1 ao índice para passar para próxima linha da tabela, e reseta o valor da variável resposta, encerra se exceder o índice
    indice += 1
    resposta = ()
    