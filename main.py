
arquivo = open('frases.txt', 'r')

contador = 1

for linha in arquivo:
    linha = arquivo.readline()
    linha = linha.strip()
    if linha:
       print(contador, linha) 
       contador += 1


arquivo.close()