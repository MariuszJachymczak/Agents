from typing import Sequence
from langchain_openai import ChatOpenAI
from langgraph.graph.message import MessageGraph
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# Funkcja sprawdzająca słowo "Pomidor"
def check_for_pomidor(messages: Sequence[HumanMessage | AIMessage]):
    last_message = messages[-1]
    if isinstance(last_message, HumanMessage) and "Pomidor" in last_message.content:
        # Dodajemy wiadomość AI z odpowiedzią "Tomato"
        return [AIMessage(content="Tomato")]
    return []

# Funkcja modelu
def call_model(messages: Sequence[HumanMessage | AIMessage]):
    # Wywołanie modelu z listą wiadomości
    response = model.invoke(messages)
    return [response]

# Inicjalizacja modelu
model = ChatOpenAI(model="gpt-3.5-turbo", streaming=True)

# Tworzenie grafu wiadomości
workflow = MessageGraph()

# Dodanie węzłów
workflow.add_node("check_pomidor", check_for_pomidor)
workflow.add_node("agent", call_model)

# Ustawienie punktu wejścia
workflow.set_entry_point("check_pomidor")

# Dodanie krawędzi pomiędzy węzłami
workflow.add_edge("check_pomidor", "agent")

# Ustawienie punktu końcowego
workflow.set_finish_point("agent")

# Wejściowe wiadomości
inputs = [HumanMessage(content="cześć ziomuś co tam Pomidorze?")]

# Kompilacja aplikacji
app = workflow.compile()
app.get_graph().draw_mermaid_png(output_file_path="tomato1.png")

# Wywołanie aplikacji
outputs = app.invoke(inputs)

# Iterowanie po liście wyników
for message in outputs:  # Tutaj outputs jest listą
    if isinstance(message, HumanMessage):
        print(f"Człowiek: {message.content}")
    elif isinstance(message, AIMessage):
        print(f"ChatGPT: {message.content}")
