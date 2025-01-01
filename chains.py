from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

reflection_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a viral twitter influencer grading a tweet. Generate critique and recomendations for the users tweet."
        "Always provide detailed reocmmendations, including requests for length, virality style, and tone."
     ),
    MessagesPlaceholder(variable_name='messages'),
    ]
)

generation_prompt = ChatPromptTemplate.from_messages([(
    "system",
    "You are a techie influencer assistant tasked with excellent twitter posts."
    "Generate the best twitter post possible for user`s request."
    "If the user provides critique, respond with a revised version of your previous attempts."
),
MessagesPlaceholder(variable_name='messages'),
    ]
)

llm = ChatOpenAI()

generate_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm


