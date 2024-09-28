from dotenv import load_dotenv
from fasthtml.common import *
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

app, rt = fast_app()

messages = []

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

headers = [
    Script(src="https://cdn.tailwindcss.com"),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css",
    ),
    Link(rel="icon", href="robot.png", type="image/png"),
    Script(src="https://unpkg.com/htmx.org@1.6.1/dist/htmx.min.js")
]

def ChatMessage(msg):
    bubble_class = (
        "chat-bubble-primary"
        if isinstance(msg, HumanMessage)
        else "chat-bubble-secondary"
    )
    align_class = "chat-end" if isinstance(msg, HumanMessage) else "chat-start"
    return Div(
        Div(
            Div(msg.content, cls=f"chat-bubble {bubble_class}"),
            cls=f"chat {align_class}",
        ),
        cls="mb-2",
    )


@rt("/")
def get():
    input = Input(
        type="text",
        name="user_input",
        onfocus="this.value=''",
        placeholder="Enter your message...",
        cls="input w-full"
    )
    button = Button(
        "Send",
        cls="btn btn-primary w-full mt-2"
    )
    form = Div(
        Form(
            input,
            button,
            method="post",
            action="/chat",
            hx_post="/chat",
            hx_target="#chat-history-container",
            hx_swap="innerHTML",
            cls="mt-4"
        ),
        cls="w-full max-w-lg mx-auto"
    )
    chat_history = Div(
        *[ChatMessage(msg) for msg in messages], 
        id="chat-history"
    )
    chat_container = Div(
        chat_history,
        id="chat-history-container",
        cls="mt-4 w-full max-w-lg mx-auto bg-white p-4 shadow-md rounded-lg overflow-y-auto"
    )
    html = Html(
        *headers,
        H1("Chat with Me", cls="text-center"),
        Div(
            Img(src="ME.webp", cls="w-24 h-24 mx-auto"),
            cls="flex justify-center mt-4"
        )
    )
    chat = Titled(
        html,
        form,
        chat_container
    )
    return chat

@rt("/chat", methods=["post"])
def chat(user_input: str):#
    if user_input:
        messages.insert(0, HumanMessage(content=user_input))

        response = llm.invoke(
            [SystemMessage(content="Respond like a human."), *messages]
        )

        messages.insert(0, AIMessage(content=response.content))
                
        return Div(*[ChatMessage(msg) for msg in messages], id="chat-history")
        
serve()