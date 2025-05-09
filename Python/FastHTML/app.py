from fasthtml.common import *
from components import *
comp = components
app, routes = fast_app()

tasklist = []

@routes("/")
def homepage():
    task = comp.create_form("text", "task", "Insert the task to be add...", 
                       "Send", "post", "/add_task", "task-list", "outerHTML")
    element_tasklist = comp.create_tasklist(tasklist, "Delete", "/delete_task", "task-list", "outerHTML")
    form = Titled("TaskList", task, element_tasklist)    
    return form

@routes("/add_task", methods=["post"])
def add_task(task: str):
    if task:
        tasklist.append(task)
    return comp.create_tasklist(tasklist, "Delete", "/delete_task", "task-list", "outerHTML")

@routes("/delete_task/{id}", methods=["get"])
def delete(id:int):
    if len(tasklist)>id:
        tasklist.pop(id)
    return comp.create_tasklist(tasklist, "Delete", "/delete_task", "task-list", "outerHTML")

@routes("/about")
def about():
    return comp.create_title("About", "About FastHTML", "Lorem Ipsum is simply dummy text of the printing about FastHTML")

@routes("/images")
def images():
    image = Titled("Images")
    return image

@routes("/teste")
def teste():
    return Div(
        "Teste",
        id="teste"
    )

serve()