<h1>Automatizar tarefas (UIAutomation)</h1>

<h3>Capturar os elementos clicados pelo mouse para usar como base na automatização de tarefas.</h3>

## 🔧 Funções

- Capturar elementos clicado na tela
- Imprimir detalhes dos elementos para utilizar na automatização
- Automatizar tarefas

## Descrição
Ao utilizar o inspector.py, cada clique do mouse é apresentado no terminal para ser utilizado na automatizaão de tarefas.
No exemplo abaixo, temos os dados do botao cancelar deuma janela.
-------------------------------
Elemento Encontrado: Cancelar
  Name (Título): Cancelar
  ControlType: 50000
  AutomationId: 
  ClassName: QPushButton
  NativeWindowHandle (HWND): 0
  Caminho (Path): Área de Trabalho 1 (PaneControl - ID: ) -> Usuário 1 - Anki (WindowControl - ID: MainWindow) -> Exportar (WindowControl - ID: MainWindow.ExportDialog) ->  (GroupControl - ID: MainWindow.ExportDialog.buttonBox) -> Cancelar (ButtonControl - ID: )
-------------------------------
Com os dados acima é possível configurar a automação utilizando o exemplo abaixo:
-------------------------------
def automatizar():
    janela = uia.WindowControl(searchDepth=1, Name="Usuário 1 - Anki")
    #Pode ser utilizado *AutomationID* caso o dado seja capturado
    menu = janela.MenuItemControl(Name="Arquivo")
    menu.Click()
    time.sleep(0.5)
    submenu = janela.MenuItemControl(Name="Exportar")
    submenu.Click()
    time.sleep(0.5)
    btnCancelar = janela.ButtonControl(Name="Cancelar")
    btnCancelar.Click()
-------------------------------

## 👨‍💻 Tecnologias Utilizadas

Utilizando apenas **PYTHON** e as bibliotecas:
> - UIAutomation
> - Time
> - Keyboard
> - Mouse


## 📜 Conteúdo

> - Baixar o projeto
> - Abra o VSCode e depois selecione File->Open Folder e escolha a pasta criada para o projeto
> - Abra o terminal no menu Terminal->New Terminal
> - Instale o ambiente virtual com o comando no terminal aberto: python -m venv venv
> - Após criar a pasta "venv", execute o comando no terminal aberto: venv/scripts/activate
> - O ambiente virtual será iniciado e ficará no prompt do terminal "(venv) c:\...\Pasta_Criada"
> - Para instalação das bibliotecas do projeto, ainda no terminal execute o comando: pip install -r requirements.txt
> - Para executar os arquivos do Python, use o comando: python -m <nome_arquivo.py>

## Atenção ##

> - Para aprender mais sobre as ferramentas utilizadas, acesse:

<a href = "https://docs.python.org/3/">Python</a></br>
<a href = "https://github.com/yinkaisheng/Python-UIAutomation-for-Windows">UIAutomation</a></br>
<a href = "https://docs.python.org/3/library/time.html">Time</a></br>
<a href = "https://thepythoncode.com/article/control-keyboard-python">Keyboard</a></br>
<a href = "https://thepythoncode.com/article/control-mouse-python">Mouse</a></br>

> - Instalações necessárias:
<a href = "https://www.python.org/downloads/">Python</a>