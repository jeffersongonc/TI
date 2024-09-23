import os
from dotenv import load_dotenv
from fasthtml.common import *
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or None

app, rt = fast_app()

messages = []

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
#llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
headers = [
    Script(src="https://cdn.tailwindcss.com"),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css",
    ),
    Link(rel="icon", href="robot.png", type="image/png"),
    Script(src="https://unpkg.com/htmx.or@1.6.1/dist/htmx.min.js")
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
        cls="mb-s",
    )


@rt("/")
def get():
    chat_form = Form(
        Input(
            type="text",
            name="user_input",
            placeholder="Enter your message...",
            cls="input w-full",
        ),
        Button("Send", cls="btn btn-primary w-full mt-2"),
        method="post",
        action="/chat",
        hx_post="/chat",
        hx_target="#chat-history-container",
        hx_swap="innerHTML",
        cls="mt-4",
    )

    chat_history = Div(*[ChatMessage(msg) for msg in messages], id="chat-history")

    return Html(
        *headers,
        H1("Chat with Robot", cls="text-2x1"),
        Div(
            Img(src="robot.png", cls="w-16 h-16 mx-auto"),
            cls="flex justify-center mt-4",
        ),
        Div(chat_form, cls="w-full max-w-lg mx-auto"),
        Div(
            chat_history,
            id="chat-history-container",
            cls="mt-4 w-full max-w-lg mx-auto bg-white p4 shadow-md rounded-lg overflow-y-auto",
        ),
    )


@rt("/chat", methods=["post"])
def chat(user_input: str):
    if user_input:
        messages.append(HumanMessage(content=user_input))

        response = llm.invoke(
            [SystemMessage(content="Respond like a robot."), *messages]
        )

        messages.append(AIMessage(content=response.content))

        return Div(*[ChatMessage(msg) for msg in messages])
    
    
serve()