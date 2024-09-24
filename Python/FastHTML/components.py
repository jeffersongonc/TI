from fasthtml.common import *

class components:
    def __init__(self):
        pass

    def create_title(title:str, subtitle: str, text: str):
        title = Div(
            H1(title),
            P(subtitle),
            P(text)
        )
        return title

    def create_form(inputType:str, inputName:str, inputPlaceHolder:str, 
                    buttonText:str, inputMethod:str, inputAction:str,
                    target:str, swap:str):
        comp = components
        form = Form(
            comp.create_input(inputType, inputName, inputPlaceHolder),
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

    def create_input(inputType: str, inputName: str, inputPlaceHolder: Optional[str] = ""):
        if (inputType not in ["button", "checkbox", "color" , "date" , "datetime-local",
                              "email" , "file"    , "hidden", "image", "month", "url"  ,
                              "number", "password", "radio" , "range", "reset", "week" ,
                              "search", "submit"  , "tel"   , "text" , "time" ]):
            input = P("Valor fora da faixa.")
            return input
        
        input = Input(type=inputType, name=inputName, placeholder=inputPlaceHolder)
        return input

        