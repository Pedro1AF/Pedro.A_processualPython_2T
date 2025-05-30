import random #importei random
jogadores = [] #lista com os jogadores
while len(jogadores) <= 5: 
#acima o while para repetir o input utilizando como parametro o len que conta o numero de jogadores
    nomes = jogadores.append(input("Insira os 6 jogadores: "))
     #acima um input com append para adicionar os valores de entrada para a lista
     
assasino = random.choice(jogadores)
#randomiza um jogador para assasino
xerife = random.choice(jogadores)
#randomiza um jogador para xerife


print(f"Os jogadores são: {jogadores}, e o assasino é {assasino}, e o xerife {xerife}")
#printa todos os jogadores e os dois especiais
