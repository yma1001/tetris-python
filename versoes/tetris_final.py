# Importação de bibliotecas.
import numpy as np
import random
import curses
import time
# Início de função do jogo.
def jogo_tetris(tela):
    curses.curs_set(0)
    curses.start_color()
    tela.nodelay(True)

    # Criação das peças e configuração de suas cores respectivas.
    # Cores identificadas pela numeração de cada peça.
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    peca_i = np.array([[1], [1], [1], [1]])

    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    peca_q = np.array([[2, 2], [2, 2]])

    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    peca_t = np.array([[3, 3, 3], [" ", 3, " "]])

    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    peca_s = np.array([[" ", 4, 4], [4, 4, " "]])

    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
    peca_z = np.array([[5, 5, " "], [" ", 5, 5]])

    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)
    peca_j = np.array([[6, " ", " "], [6, 6, 6]])

    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
    peca_l = np.array([[" ", " ", 7], [7, 7, 7]])

    # Cor das paredes, ou limites do tabuleiro, e da peça bomba.
    curses.init_pair(8, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(9, curses.COLOR_RED, curses.COLOR_BLACK)
    # Criação de peça bomba, sendo um bloco único.
    peca_b = np.array([[9]])
    # Lista de peças que servirá para o sorteio de peças posteriormente.
    lista_pecas = [peca_i, peca_q, peca_t, peca_s, peca_z, peca_j, peca_l, peca_b]
    num_linhas, num_colunas = 20, 10

    # Inicialização do tabuleiro e da pontuação.
    tabuleiro = np.full((num_linhas, num_colunas), ' ')
    pontuacao = 0

    # Gera a primeira e a próxima peça ao mesmo tempo.
    peca_da_vez = random.choice(lista_pecas)
    proxima_peca = random.choice(lista_pecas)
    # Início de loop principal.
    while True:
        # Sorteio da posição que a peça irá aparecer.
        posicao = random.randint(0, num_colunas - peca_da_vez.shape[1])
        linha_atual = 0 # Linha atual começa com zero.
        # Loop secundário.
        while True:
            tela.clear()

            # Desenhar as paredes.
            for i in range(num_linhas + 2):
                tela.addch(i, 0, '█', curses.color_pair(8))  # Parede esquerda
                tela.addch(i, num_colunas + 1, '█', curses.color_pair(8))  # Parede direita
            for j in range(num_colunas + 2):
                tela.addch(0, j, '█', curses.color_pair(8))  # Parede superior
                tela.addch(num_linhas + 1, j, '█', curses.color_pair(8))  # Parede inferior

            # Exibe o tabuleiro.
            for i in range(num_linhas):
                for j in range(num_colunas):
                    if tabuleiro[i, j] != ' ':
                        tela.addch(i + 1, j + 1, '█', curses.color_pair(int(tabuleiro[i, j])))

            # Exibe a peça atual.
            for i, row in enumerate(peca_da_vez):
                for j, val in enumerate(row):
                    if val != " ":
                        tela.addch(linha_atual + i + 1, posicao + j + 1, '█', curses.color_pair(int(val)))

            # Exibe a pontuação e a próxima peça ao lado do tabuleiro.
            tela.addstr(1, num_colunas + 3, f"Pontuação: {pontuacao}")
            tela.addstr(3, num_colunas + 3, "Próxima peça:")
            for i, row in enumerate(proxima_peca):
                for j, val in enumerate(row):
                    if val != " ":
                        tela.addch(4 + i, num_colunas + 3 + j, '█', curses.color_pair(int(val)))

            # Exibe as instruções de botões do jogo.
            tela.addstr(10, num_colunas + 3, "Controles:")
            tela.addstr(11, num_colunas + 3, "A - Esquerda")
            tela.addstr(12, num_colunas + 3, "D - Direita")
            tela.addstr(13, num_colunas + 3, "S - Descer")
            tela.addstr(14, num_colunas + 3, "Espaço - Rotacionar")

            tela.refresh() # Atualiza o terminal.
            time.sleep(0.5) #Tempo que todo o código funciona.

            tecla = tela.getch() # Captura a tecla do usuário.
            # Todas as possíveis teclas que podem ser utilzadas.
            if tecla == ord("a"):
                posicao = max(0, posicao - 1)
            elif tecla == ord("d"):
                posicao = min(num_colunas - peca_da_vez.shape[1], posicao + 1)
            elif tecla == ord("s"):
                linha_atual += 1
            elif tecla == ord(" "):
                # Realiza uma rotação.
                peca_rotacionada = np.rot90(peca_da_vez)

                # Verificação da peça rotacionada, se ela cabe dentro dos limites laterais.
                if posicao + peca_rotacionada.shape[1] <= num_colunas:
                    peca_da_vez = peca_rotacionada  # Aplica a rotação se for seguro.
            # A peça desce uma linha.
            linha_atual += 1  
            # Verificação para identificar se a peça chegou ao fim do tabuleiro.
            if linha_atual + peca_da_vez.shape[0] > num_linhas or any(
                linha_atual + i < num_linhas and tabuleiro[linha_atual + i, posicao + j] != ' '
                for i, row in enumerate(peca_da_vez)
                for j, val in enumerate(row) if val != " "
            ):
                linha_atual -= 1

                # Tratamento especial para a peça bomba.
                if np.array_equal(peca_da_vez, peca_b):
                    for i in range(max(0, linha_atual - 1), min(num_linhas, linha_atual + 2)):
                        for j in range(max(0, posicao - 1), min(num_colunas, posicao + 2)):
                            tabuleiro[i, j] = ' '  # Limpa a área ao redor da bomba
                else:
                    for i, row in enumerate(peca_da_vez):
                        for j, val in enumerate(row):
                            if val != " " and linha_atual + i < num_linhas:
                                tabuleiro[linha_atual + i, posicao + j] = val
                break

        # Checa e remove linhas completas.
        linhas_completas = 0
        for i in range(num_linhas):
            if all(tabuleiro[i, j] != ' ' for j in range(num_colunas)):
                tabuleiro = np.delete(tabuleiro, i, 0)
                nova_linha = np.full((1, num_colunas), ' ')
                tabuleiro = np.vstack((nova_linha, tabuleiro))
                linhas_completas += 1

        # Atualiza a pontuação de acordo com as linhas completas.
        if linhas_completas == 1:
            pontuacao += 100
        elif linhas_completas == 2:
            pontuacao += 300
        elif linhas_completas == 3:
            pontuacao += 500
        elif linhas_completas == 4:
            pontuacao += 800

        # Verifica se o jogo terminou.
        if any(tabuleiro[0, j] != ' ' for j in range(num_colunas)):
            break

        # Passa a próxima peça para a peça atual e gera uma nova próxima peça.
        peca_da_vez = proxima_peca
        proxima_peca = random.choice(lista_pecas)

    tela.addstr(10, 0,f"Jogo Finalizado! Pontuação total: {pontuacao}", curses.color_pair(1)) # Mensagens ao fim do jogo.
    tela.refresh()
    tela.nodelay(False)
    tela.getch()

curses.wrapper(jogo_tetris)

# Autor: Yago Mendes de Araujo
# Componente Curricular: MI Algoritmos
# Concluído em: 27/10/2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.