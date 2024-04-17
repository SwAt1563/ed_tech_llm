from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMChain
from langchain import PromptTemplate
from .prompt_template import template
import os


def convert_chat_history_cp_to_lc(cp_messages, lc_memory):
    lc_memory.clear()
    for cp_message in cp_messages:
        if cp_message["role"] == "user":
            lc_memory.chat_memory.add_user_message(cp_message["content"])
        elif cp_message["role"] == "assistant":
            lc_memory.chat_memory.add_ai_message(cp_message["content"])


class ChatAPIView(APIView):
    def post(self, request):
        question = request.data.get('question', '')

        if not question:
            return Response({'answer': 'No query provided'})

        # Retrieve chat history from session or initialize if not present
        current_history = request.session.get('chat_history', [])

        # Initialize the ConversationBufferWindowMemory
        memory = ConversationBufferWindowMemory(k=30, memory_key="chat_history", return_messages=True)

        convert_chat_history_cp_to_lc(current_history, memory)

        # Setup for the AzureChatOpenAI
        llm = AzureChatOpenAI(deployment_name=os.environ['DEPLOYMENT_NAME'], temperature=0.7)

        prompt_template = PromptTemplate(
            template=template,
            input_variables=["context", "chat_history", "question"],
        )

        # Initialize the LLM chain
        conversation = LLMChain(
            llm=llm,
            prompt=prompt_template,
            verbose=True,
            memory=memory,
        )

        spam = False
        try:
            # Attempt to get the answer from the conversation dictionary.
            answer = conversation({'question': question})['text']
        except Exception as e:
            spam = True
            # Handle other general exceptions that might occur.
            answer = f"Whoopsie! It looks like you asked something I cannot answer. That's because we want to make sure everything here is super safe and fun for everyone. Is there anything else I can help with?"

        if not spam:
            current_history.append({'role': 'user', 'content': question})
            current_history.append({'role': 'assistant', 'content': answer})

        # Update and serialize the history back into the session
        request.session['chat_history'] = current_history[-30:]
        # Make sure the session is saved
        request.session.modified = True

        # Return the AI's response
        return Response({"answer": answer})
