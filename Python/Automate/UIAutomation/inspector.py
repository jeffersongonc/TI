import uiautomation as uia
import time
import keyboard
import mouse

def getElementPath(control):
    path = []
    current = control
    while current:
        # Formata o nome, o tipo e ID para cada nível da hierarquia
        path.insert(0, f"{current.Name} ({current.ControlTypeName} - ID: {current.AutomationId})")
        # Move para o elemento pai
        current = current.GetParentControl()
        # Limita para evitar caminhos excessivamente longos (até 10 níveis)
        if len(path) > 10:
             path.insert(0, "...")
             break
    
    return " -> ".join(path)

def logElementMouseClick():
    print("--- INSPETOR DE ELEMENTOS INICIADO ---")
    print("Mova o cursor e clique sobre um elemento para registrar as propriedades.")
    print("Pressione **ESC** a qualquer momento para sair.")
    
    desktop = uia.GetRootControl()

    while True:
        # Verifica se a tecla ESC foi pressionada
        if keyboard.is_pressed('esc'):
            print("\n--- INSPETOR DE ELEMENTOS FINALIZADO ---")
            break

        if mouse.is_pressed():
            try:
                # 1. Obtém o controle que está na posição atual do mouse
                control = uia.ControlFromCursor()

                print("\n" + "="*50)
                print(f"**Elemento Encontrado:** {control.Name}")
                print("="*50)
                
                # 2. Imprime as propriedades mais importantes para a automação
                print(f"  > Name (Título): **{control.Name}**")
                print(f"  > ControlType: **{control.ControlType}**")
                print(f"  > AutomationId: **{control.AutomationId}**")
                print(f"  > ClassName: {control.ClassName}")
                print(f"  > NativeWindowHandle (HWND): {control.NativeWindowHandle}")
                
                # 3. Opcional: Imprime o caminho (path) para o elemento
                path = getElementPath(control) 
                print(f"  > Caminho (Path): {path}")

            except Exception as e:
                print(f"\nErro ao inspecionar o elemento: {e}")
            
            # Aguarda um momento para evitar múltiplos logs (debounce)
            time.sleep(1)

        # Pequeno atraso para não sobrecarregar o CPU
        time.sleep(0.1)

def automatizar():
    janela = uia.WindowControl(searchDepth=1, Name="Usuário 1 - Anki")#Pode ser utilizado AutomationID caso o dado seja capturado
    menu = janela.MenuItemControl(Name="Arquivo")
    menu.Click()
    time.sleep(1)
    submenu = janela.MenuItemControl(AutomationId="MainWindow.actionExport")
    submenu.Click()
    time.sleep(1)
    btnCancelar = janela.ButtonControl(Name="Cancelar")
    btnCancelar.Click()

# Chame a função para iniciar a coleta:
if __name__ == '__main__':
    logElementMouseClick()
    #ou
    #automatizar()