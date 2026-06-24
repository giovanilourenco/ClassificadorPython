import os
import shutil

#Caminho que será organizado
pasta = r"C:\Users\Cliente\Downloads"

#Extensões
tipos = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".avi", ".mvk"],
    "Outros": [".py", ".ipynb", ".exe"]
}

#Percorre todos os arquivos disponíveis na pasta
for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)

    #Ignora pastas
    if os.path.isfile(caminho_arquivo):
        extensao = os.path.splitext(arquivo)[1].lower()

        for categoria, extensoes in tipos.items():
            if extensao in extensoes:
                pasta_destino = os.path.join(pasta, categoria)

                #Cria a pasta caso não exista
                os.makedirs(pasta_destino, exist_ok=True)

                #Move o arquivo
                shutil.move(
                    caminho_arquivo,
                    os.path.join(pasta_destino, arquivo)
                )

                print(f"{arquivo} -> {categoria}")

                break
print("Organizado!")