import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or NONE

def llm_openai():
    mensagens = [
        SystemMessage("Traduza o texto a seguir para inglês"),
        HumanMessage("Olá mundo!")
    ]

    modelo = ChatOpenAI(model="gpt-3.5-turbo")

    resposta = modelo.invoke(mensagens)

    print(resposta)

def llm_gemini_ai():
    #mensagens = [
    #    SystemMessage("Traduza o texto a seguir para inglês"),
    #    HumanMessage("Como vai você?")
    #]

    modelo = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    parser = StrOutputParser()
       
    #resposta = modelo.invoke(mensagens)
    #texto = parser.invoke(resposta)
    template_mensagens = ChatPromptTemplate.from_messages([
        ("system", "Traduza o texto a seguir para {idioma}"),
        ("user", "{texto}"),
    ])
    #template_mensagens.invoke()
    chain = template_mensagens | modelo | parser
    texto = chain.invoke({"idioma": "responder separadamente a data da ocorrência, hora, nome do paciente, somente o nome de quem fez o contato e se fez depósito", "texto": "DATA DA OCORRENCIA: 06/08/2024 / HORA: 12:20 / NOME DO PACIENTE: JEFFERSON DA SILVA GONÇALVES / SETOR: ALA 5 / DEPOSITOU?: SIM / DESCRICAO DA OCORRENCIA: HOJE A MAE DA PACIENTE RECEBEU UMA LIGAÇÃO NO CELULAR DE UMA PESSOA CHAMADA JOAO QUE IDENTIFICOU_SE COMO CARDIOLOGISTA"})
    print("TEXTO: DATA DA OCORRENCIA: 06/08/2024 / HORA: 12:20 / NOME DO PACIENTE: JEFFERSON / SETOR: ALA 5 / DEPOSITOU?: SIM / DESCRICAO DA OCORRENCIA: HOJE A MAE DA PACIENTE RECEBEU UMA LIGAÇÃO NO CELULAR DE UMA PESSOA CHAMADA JOAO QUE IDENTIFICOU_SE COMO CARDIOLOGISTA")
    print("PERGUNTA: Responder separadamente a data da ocorrência, hora, somente o nome do paciente, nome de quem fez o contato e se fez depósito")
    print(texto)

llm_gemini_ai()
