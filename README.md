# 📂 Organizador de Arquivos com Python

Automação simples desenvolvida em Python para classificar e organizar arquivos automaticamente de acordo com sua extensão.

## 💻Funcionalidades
* Organiza arquivos automaticamente em pastas específicas.
* Cria as pastas de destino caso não existam.
* Separa arquivos por categoria:
  * 📷 Imagens
  * 📄 Documentos
  * 🎥 Vídeos
  * ⚙️ Outros [otimização em progresso]
Exibe no terminal quais arquivos foram movidos.

## 🛠️ Tecnologias Utilizadas
* Python 3
* Biblioteca os
* Biblioteca shutil

## 🗃️ Estrutura
Antes da execução:
Downloads/ <br>
├── foto.jpg <br>
├── curriculo.pdf <br>
├── video.mp4 <br>
├── script.py <br>

Após a execução:

Downloads/ <br>
├── Imagens/ <br>
│   └── foto.jpg <br>
│ <br>
├── Documentos/ <br>
│   └── curriculo.pdf <br>
│<br>
├── Videos/<br>
│   └── video.mp4<br>
│<br>
└── Outros/<br>
    └── script.py<br>

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos de:
* Manipulação de arquivos e diretórios
* Estruturas de repetição (for)
* Estruturas condicionais (if)
* Dicionários
* Bibliotecas nativas do Python
* Automação de tarefas

# 💻 Como Utilizar
1. Copie o arquivo classificador.py para a pasta que deseja organizar.
2. Execute o script:
- python classificador.py
3. O programa identificará automaticamente o diretório atual e organizará os arquivos em categorias.

<img src='gif.gif'></img>

O caminho é obtido automaticamente utilizando:
- pasta = os.getcwd()
Assim, o usuário não precisa editar o código para escolher a pasta a ser organizada.
