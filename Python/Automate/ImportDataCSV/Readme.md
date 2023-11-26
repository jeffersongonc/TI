<h1>Automatizar Cadastros (Origem CSV)</h1>

<h3>Realizar o cadastro de produtos com base em dados do CSV para uma aplicação web através de funções do Python.</h3>

## 🔧 Funções

- Descobrir posições do cursor na janela
- Abrir o navegador Chrome
- Acessar página do sistema de cadastro
- Realizar login no sistema de cadastro
- Ler o arquivo *.csv
- Cadastrar os produtos do arquivo *.csv (do primeiro ao último)


## 👨‍💻 Tecnologias Utilizadas

Utilizando apenas **PYTHON** e as bibliotecas:
> - PyAutogui
> - Time
> - Pandas


## 📜 Conteúdo

> - Baixar o projeto
> - Abra o VSCode e depois selecione File->Open Folder e escolha a pasta criada para o projeto
> - Abra o terminal no menu Terminal->New Terminal
> - Instale o ambiente virtual com o comando no terminal aberto: python -m venv venv
> - Após criar a pasta "venv", execute o comando no terminal aberto: venv/scripts/activate
> - O ambiente virtual será iniciado e ficará no prompt do terminal "(venv) c:\...\Pasta_Criada"
> - Para instalação das bibliotecas do projeto, ainda no terminal execute o comando: pip install -r requirements.txt
> - Para executar os arquivos do Python, use o comando: python -m <nome_arquivo.py>

*** Atenção ***
- Para identificar a posição dos campos no navegador, abra o site e posteriormente execute o findposition.py para clicar nos campos e coletar qual a posição na sua janela. Estas referências serão usadas nas funções "pyautogui.click(x=0, y=0)".

Para aprender mais sobre as ferramentas utilizadas, acesse:

<a href = "https://docs.python.org/3/">Python</a>
<a href = "https://pyautogui.readthedocs.io/en/latest/">PyAutogui</a>
<a href = "https://pandas.pydata.org/docs/index.html">Pandas</a>
<a href = "https://docs.python.org/3/library/time.html">Time</a> 

Instalações necessárias:
<a href = "https://www.python.org/downloads/">Python</a>