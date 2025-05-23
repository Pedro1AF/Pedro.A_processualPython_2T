entradas = [1, 2, 3, 4, 5]
print("Olá, como posso te chamar?")
entradas[0] = input("Seu nome:")

print("Qual seu linkedin?")
entradas[1] = input("Seu nome no linkedin:")

print("Em qual cargo está atualmente?")
entradas[2] = input("Insira seu cargo:")

print("Qual a empresa de atuação?")
entradas[3] = input("Sua empresa:")

print("Onde mora?")
entradas[4] = input("Insira seu endereço:")

print(f"Olá {entradas[0]}")
print(f"estamos buscando vagas para {entradas[2]}")
print(f"nas proximidades de {entradas[4]}") 
print(f"priorizando próximas a {entradas[3]}")
print(f"caso encontremos registraremos em seu linkedin {entradas[1]}")
