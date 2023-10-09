import streamlit as st
from PIL import Image
from gradio_client import Client

image = Image.open('bíblia1.jpg')

# Título da aplicação Streamlit
st.title("Chatbot da Bíblia Sagrada")
st.image('bíblia1.jpg', caption='Biblia Sagrada')

# Criar um campo de entrada de texto para a pergunta
question = st.text_input("Digite sua pergunta:")

# Botão para fazer a previsão
if st.button("Enviar"):
    # Criar uma instância do cliente Gradio
    client = Client("FabioSantos/biblia", hf_token="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")
    
    # Fazer uma previsão com a pergunta inserida
    result = client.predict(question, api_name="/predict")
    
    # Exibir a resposta
    st.write("Resposta do Chatbot:")
    st.write(result)

# Nota explicativa
st.markdown("*Desenvolvido por Prof.Dr.Fabio Santos (fssilva@uea.edu.br)*")
