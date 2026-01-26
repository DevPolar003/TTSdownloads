import os
from gtts import gTTS

arquivo = open('frases.txt', 'r')
contador = 1
frases = []
nomePasta = "frasesAudios"

if not os.path.exists(nomePasta):
  os.makedirs(nomePasta)
  print(f"Pasta {nomePasta} criada com sucesso!") 

for linha in arquivo:
    linha = linha.strip()
    if linha:
       print(contador, linha) 
       frases.append(linha)
       contador += 1
    

frasesFormatadas = []

for frase in frases:
    nomeArquivo = frase.replace("?", "").replace(" ", "_")
    frasesFormatadas.append(nomeArquivo)
    caminhoCompleto = os.path.join(nomePasta, nomeArquivo + ".mp3")
    audio = gTTS(text=frase, lang='fr')
    audio.save(caminhoCompleto)

arquivo.close()

