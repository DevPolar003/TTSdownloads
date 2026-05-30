import os
from gtts import gTTS

VERSION = "1.0.0"
idioma_atual = "fr"  

def exibir_ajuda():
    print("\nComandos disponíveis:")
    print("  download           - Inicia o download dos áudios a partir do 'frases.txt'")
    print("  lang [código]      - Altera o idioma do TTS (ex: pt, en, fr, es)")
    print("  version            - Exibe a versão atual do CLI")
    print("  help               - Mostra esta tela de ajuda")
    print("  exit               - Encerra o programa")


print("========================")
print("   TTS DOWNLOADS CLI    ")
print("========================")
print("Digite 'help' para ver os comandos disponíveis.")

while True:
    
    entrada = input(f"\ntts ({idioma_atual}) > ").strip().lower()

    
    if not entrada:
        continue

    
    partes = entrada.split()
    comando = partes[0]
    argumentos = partes[1:] if len(partes) > 1 else []

   
    if comando == "help":
        exibir_ajuda()

    
    elif comando == "version":
        print(f"TTS Downloads CLI - Versão {VERSION}")

    
    elif comando == "lang":
        if argumentos:
            idioma_atual = argumentos[0]
        else:
           
            novo_idioma = input("Digite o código do idioma (ex: pt, en, es, fr): ").strip().lower()
            if novo_idioma:
                idioma_atual = novo_idioma
        print(f"Idioma alterado com sucesso para: {idioma_atual}")

    
    elif comando == "download":
        frases = []
        nomePasta = "frasesAudios"

        if not os.path.exists(nomePasta):
            os.makedirs(nomePasta)
            print(f"Diretório {nomePasta} criado com sucesso.") 
  
        try:   
            with open('frases.txt', 'r', encoding='utf-8') as arquivo:  
                for linha in arquivo:
                    linha = linha.strip()
                    if linha:
                        frases.append(linha)

            if not frases:
                print("O arquivo 'frases.txt' está vazio.")
                continue

            print(f"\nIniciando processamento em [{idioma_atual}]...")

            for frase in frases:
                nomeArquivo = frase.replace("?", "").replace("!", "").replace(" ", "_")
                caminhoCompleto = os.path.join(nomePasta, nomeArquivo + ".mp3")

                
                audio = gTTS(text=frase, lang=idioma_atual)
                audio.save(caminhoCompleto)
                print(f"Salvo: {nomeArquivo}.mp3")

            print(f"\nDownloads concluídos com sucesso na pasta: {nomePasta}")   
        
        except FileNotFoundError:
            print("Erro: O arquivo 'frases.txt' não foi encontrado.")
        except Exception as e:
            print(f"Algo deu errado: {e}")

    
    elif comando == "exit":
        print("Saindo... Até logo!")
        break
    
    
    else:
        print(f"Comando '{comando}' não reconhecido. Digite 'help' para ver a lista.")
