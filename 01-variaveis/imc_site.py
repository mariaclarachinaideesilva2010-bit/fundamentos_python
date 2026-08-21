import streamlit as st

# Título da página
st.title('Calculadora de IMC')

# Texto Explicativo
st.write('Minha primeira página')

# Input de dados
nome = st.text_input('Digite seu nome: ')

# Botão
if st.button ('Enviar'):
    if nome:
        st.success(f'Olá {nome} Seja Bem-Vindo!!!')
    else:
        st.warning('Gentileza, digitar um nome!')    