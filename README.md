# tetris-python
Tetris game implemented in Python using NumPy. Academic project at UEFS.
# 🟦 Tetris em Python no Terminal (NumPy + Curses)

Este é um jogo clássico de **Tetris** desenvolvido em **Python**, utilizando as bibliotecas `NumPy` e `curses`.  
O projeto foi desenvolvido como prática acadêmica durante a graduação em **Engenharia de Computação (UEFS)**.

---

## 🎮 Funcionalidades
- Peças clássicas do Tetris (I, O, T, S, Z, J, L)  
- Peça especial **bomba** 💣 que destrói blocos próximos  
- Tabuleiro renderizado no terminal com bordas coloridas  
- Pontuação baseada em linhas completas:
  - 1 linha = +100 pontos  
  - 2 linhas = +300 pontos  
  - 3 linhas = +500 pontos  
  - 4 linhas (Tetris) = +800 pontos  
- Exibição da **próxima peça**  
- Mensagem final com a pontuação total  

---

## 🚀 P
Para executar o código é necessário a instalação da biblioteca numpy e para windows é necessária a instalação das bibliotecas numpy e do curses.

Para instalação em linux/MacOS: pip install numpy

Para instalação em Windows (necessário suporte ao curses): pip install numpy windows-curses

Execute o jogo:python tetris.py

⌨️ Controles
A → mover para a esquerda
D → mover para a direita
S → acelerar queda
Espaço → rotacionar peça

📚 Aprendizados com o projeto
Uso da biblioteca curses para interfaces no terminal
Manipulação de matrizes com NumPy
Implementação de loops de jogo em tempo real
Lógica de colisão, rotação e pontuação do Tetris
