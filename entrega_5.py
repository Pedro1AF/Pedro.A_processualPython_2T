import re
nomes = []
    
def validar(valida):
    padrao = r'^[a-zA-ZÀ-ÿ\s]{1,20}$'
    return re.fullmatch(padrao, valida) is not None
    
while len(nomes) <= 9:
    valida = input("Insira o nome:").lower().strip()
    if not valida:
        print("Erro: O nome não pode estar vazio!")
        break
    elif len(valida) > 20:
        print("Erro: O nome deve ter no máximo 20 caracteres!")
        break
    elif not validar(valida):
        print("Erro: Use apenas letras e espaços (sem números ou caracteres especiais)!") 
        break
    else:
        lista = nomes.append(valida)
    
alfabetico = sorted(nomes)
    
contar_carac = len(nomes[0])
contar_carac1 = len(nomes[1])
contar_carac2 = len(nomes[2])
contar_carac3 = len(nomes[3])
contar_carac4 = len(nomes[4])
contar_carac5 = len(nomes[5])
contar_carac6 = len(nomes[6])
contar_carac7 = len(nomes[7])
contar_carac8 = len(nomes[8])
contar_carac9 = len(nomes[9])

print(f"abaixo a lista de nomes em ordem alfabetica: \n {alfabetico}")
print(f"{nomes[0]}, possui {contar_carac} caracteres.")
print(f"{nomes[1]}, possui {contar_carac1} caracteres.")
print(f"{nomes[2]}, possui {contar_carac2} caracteres.")
print(f"{nomes[3]}, possui {contar_carac3} caracteres.")
print(f"{nomes[4]}, possui {contar_carac4} caracteres.")
print(f"{nomes[5]}, possui {contar_carac5} caracteres.")
print(f"{nomes[6]}, possui {contar_carac6} caracteres.")
print(f"{nomes[7]}, possui {contar_carac7} caracteres.")
print(f"{nomes[8]}, possui {contar_carac8} caracteres.")
print(f"{nomes[9]}, possui {contar_carac9} caracteres.")
