import os
from gtts import gTTS
import keyboard

frases = []
nomePasta = "frasesAudios"

if not os.path.exists(nomePasta):
    os.makedirs(nomePasta)
    print(f"Directory {nomePasta} created with success") 
  
try:   
    with open('frases.txt', 'r', encoding='utf-8') as arquivo:  
        for i, linha in enumerate(arquivo, 1):
            linha = linha.strip()
            if linha:
                frases.append(linha)

    print("Processing of all phrases is starting...")

    for frase in frases:
        nomeArquivo = frase.replace("?", "").replace("!", "").replace(" ", "_")
        caminhoCompleto = os.path.join(nomePasta, nomeArquivo + ".mp3")

        audio = gTTS(text=frase, lang='fr')
        audio.save(caminhoCompleto)
        print(f"Saved: {nomeArquivo}")

except FileNotFoundError:
    print("Error: file frases.txt not found")
except Exception as e:
    print(f"Something went wrong: {e}")
else:
    print("All the downloads are finished in the directory: " + nomePasta)   
finally: 
  input("\nProcess finished. Press Enter to exit...")