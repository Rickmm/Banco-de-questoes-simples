# 🧮 Quiz Matemático

Quiz de perguntas e respostas de matemática rodando no terminal, desenvolvido em Python como projeto de aprendizado.

---

## 💡 Sobre o projeto

O programa lê 60 questões de um arquivo CSV, permite que o usuário escolha o nível de dificuldade, embaralha as questões e as apresenta uma por vez. O usuário digita a letra da alternativa correta (A, B, C ou D) e recebe feedback imediato. O quiz encerra automaticamente ao completar todas as questões, ou quando o usuário digitar **"Sair"**.

---

## ⚙️ Funcionalidades

- Escolha de nível antes de iniciar: **Fácil**, **Médio**, **Difícil** ou **Misturado**
- Questões embaralhadas a cada execução, sem repetição
- Validação de entrada — alternativas inválidas repetem a mesma pergunta
- Feedback imediato após cada resposta
- Encerramento automático ao completar todas as questões

---

## 📊 Sobre as questões

O banco conta com **60 questões de matemática** divididas em 3 níveis:

| Nível | Conteúdo | Qtd |
|-------|----------|-----|
| Fácil | Operações básicas, dobro, metade, triplo | 20 |
| Médio | Porcentagem, regra de três, geometria, juros simples, velocidade | 20 |
| Difícil | Juros compostos, PA, PG, logaritmo, trigonometria, volumes | 20 |

---

## 🗂️ Arquivos

```
├── main.py                      # Código principal do quiz
├── questionsdata_completo.csv   # Banco com todas as 60 questões
└── .gitignore
```

---

## 🚀 Como executar

**1. Clone o repositório:**
```bash
git clone https://github.com/Rickmm/Quiz-Matematica.git
```

**2. Instale as dependências:**
```bash
pip install pandas
```

**3. Execute:**
```bash
python main.py
```

---

## 🛠️ Tecnologias

- **Python 3**
- **Pandas** — leitura e manipulação do CSV

---

## 👤 Autor

Feito por **Rick** — projeto inicial de aprendizado em Python.  
