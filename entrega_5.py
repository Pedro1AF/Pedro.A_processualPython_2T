nomes = []
for i in range(1 , 5):
    teste = nomes.append(input("Digite um valor: "))
    

lista_ordenada = sorted(nomes, key=str.lower)
num_carac = len(teste)
print(f"{lista_ordenada}, possui o numero de caracteres {num_carac}")
