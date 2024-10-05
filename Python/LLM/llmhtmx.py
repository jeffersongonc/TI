import os
from dotenv import load_dotenv
from fasthtml.common import *
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from groq import Groq

load_dotenv()

# DEFAULTS OPENAI
OPENAI_API_MODEL       = os.getenv("OPENAI_API_MODEL") or None
OPENAI_API_TEMPERATURE = os.getenv("OPENAI_API_TEMPERATURE") or None
OPENAI_LLM_CONFIG      = ChatOpenAI(model=OPENAI_API_MODEL, temperature=OPENAI_API_TEMPERATURE)

# DEFAULTS GOOGLE GEMINI
GOOGLE_API_MODEL       = os.getenv("GOOGLE_API_MODEL") or None
GOOGLE_API_TEMPERATURE = os.getenv("GOOGLE_API_TEMPERATURE") or None
GOOGLE_LLM_CONFIG      = ChatGoogleGenerativeAI(model=GOOGLE_API_MODEL, temperature=GOOGLE_API_TEMPERATURE)

# DEFAULTS GROQ
GROQ_API_KEY    = os.getenv("GROQ_API_KEY"   ) or None
GROQ_API_MODEL  = os.getenv("GROQ_API_MODEL" ) or None
GROQ_API_STOP   = True if os.getenv("GROQ_API_STOP"  )== "True" else None
GROQ_API_STREAM = True if os.getenv("GROQ_API_STREAM")=="True" else False
GROQ_LLM_CONFIG = Groq(api_key=GROQ_API_KEY)

app, rt = fast_app()

messages = []

@rt("/")
def get():
    chat = Titled(
        Html_Page(),
        Form_Chat(),
        Chat_Container()
    )
    return chat

@rt("/chat", methods=["post"])
def chat(user_input: str, choice_llm: str):
    if user_input:
        try:
            messages.insert(0, HumanMessage(content=user_input))
            
            if choice_llm == "groq" :
                response = GROQ_LLM_CONFIG.chat.completions.create(
                    messages=[{"role": "system", "content": "Respond like a human."},
                            {"role": "user", "content": user_input}
                    ],
                    model=GROQ_API_MODEL,
                    stop=GROQ_API_STOP,
                    stream=GROQ_API_STREAM
                )
                
                messages.insert(0, AIMessage(content=response.choices[0].message.content))
            elif choice_llm == "gemini" :
                response = GOOGLE_LLM_CONFIG.invoke(
                    [SystemMessage(content="Respond like a human."), messages[0]]
                )
                
                messages.insert(0, AIMessage(content=response.content))
            else:
                response = OPENAI_LLM_CONFIG.invoke(
                    [SystemMessage(content="Respond like a human."), messages[0]]
                )
                
                messages.insert(0, AIMessage(content=response.content))
        except:
            messages.insert(0, AIMessage(content="Failed to use this AI, choose another option."))

    return Div(*[ChatMessage(msg) for msg in messages], id="chat-history")

# COMPONENTS HTML
def Html_Page():
    html = Html(
        *Header_Html(),
        H1("Chat with Me", cls="text-center"),
        Div(
            Img(src="ME.webp", cls="w-24 h-24 mx-auto"),
            cls="flex justify-center mt-4"
        )
    )
    
    return html

def Header_Html():
    headers = [
        Script(src="https://cdn.tailwindcss.com"),
        Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css",
        ),
        Link(rel="icon", href="robot.png", type="image/png"),
        Script(src="https://unpkg.com/htmx.org@1.6.1/dist/htmx.min.js")
    ]
    
    return headers

def Input_Choice_Llm():
    choice_llm = Div(
        Div(
            Label(
                Input(
                    type="radio",
                    id="openai",
                    name="choice_llm",
                    value="openai"
                ),
                "OpenAI",
                cls="px-2"
            ),
            cls="flex self-auto"
        ),
        Div(
            Label(
                Input(
                    type="radio",
                    id="gemini",
                    name="choice_llm",
                    value="gemini"
                ),
                "Google Gemini",
                cls="px-2"
            ),
            cls="flex self-auto"
        ),
        Div(
            Label(
                Input(
                    type="radio",
                    id="groq",
                    name="choice_llm",
                    value="groq",
                    checked=True
                ),
                "Groq",
                cls="px-2"
            ),
            cls="flex self-auto"
        ),
        cls="flex flex-row items-stretch justify-center"
    )

    return choice_llm

def Input_Chat_Text():
    input = Input(
        type="text",
        name="user_input",
        onfocus="this.value=''",
        placeholder="Enter your message...",
        cls="input w-full"
    )
    
    return input

def Button_Send_Chat():
    button = Button(
        "Send",
        cls="btn btn-primary w-full mt-2"
    )
    return button

def Form_Chat():
    form = Div(
        Form(
            Input_Choice_Llm(),
            Input_Chat_Text(),
            Button_Send_Chat(),
            method="post",
            action="/chat",
            hx_post="/chat",
            hx_target="#chat-history-container",
            hx_swap="innerHTML",
            cls="mt-4"
        ),
        cls="w-full max-w-lg mx-auto"
    )
    return form

def ChatMessage(msg):
    bubble_class = (
        "chat-bubble-primary"
        if isinstance(msg, HumanMessage)
        else "chat-bubble-secondary"
    )
    align_class = "chat-end" if isinstance(msg, HumanMessage) else "chat-start"

    div = Div(
        Div(
            Div(msg.content, cls=f"chat-bubble {bubble_class}"),
            cls=f"chat {align_class}",
        ),
        cls="mb-2",
    )

    return div

def Chat_History():
    chat_history = Div(
        *[ChatMessage(msg) for msg in messages], 
        id="chat-history"
    )
    return chat_history

def Chat_Container():
    chat_container = Div(
        Chat_History(),
        id="chat-history-container",
        cls="mt-4 w-full max-w-lg mx-auto bg-white p-4 shadow-md rounded-lg overflow-y-auto"
    )
    return chat_container

serve()