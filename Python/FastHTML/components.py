from fasthtml.common import Div, H1, P, Form, Input, Button, Ul, Li, A

def create_title(title:str, subtitle: str, text: str):
    return Div(
        H1(title),
        P(subtitle),
        P(text)
    )

def create_form(inputType:str, inputName:str, inputPlaceHolder:str, 
                buttonText:str, inputMethod:str, inputAction:str,
                target:str, swap:str):
    form = Form(
        Input(type=inputType, name=inputName, placeholder=inputPlaceHolder),
        Button(buttonText),
        method=inputMethod,
        action=inputAction,
        hx_post=inputAction,
        hx_target=f"#{target}",
        hx_swap=swap
    )
    return form
def create_tasklist(tasklist, a_text, a_href, target:str, swap:str):
    list_itens = [Li(task, " - ", A(a_text, 
                                    hx_get = f"{a_href}/{i}", 
                                    hx_target=f"#{target}", 
                                    hx_swap=swap)) for i, task in enumerate(tasklist)]
    list = Ul(
        *list_itens, id=target
    )
    return list