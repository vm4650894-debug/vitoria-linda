#criaçao de variavel
import streamlit as st

nome=st.text_input('digite seu nome')
email=st.text_input('digite seu email')

st.write(nome)

if st.button('enviar'):
    if email == 'gabrielgameplay@gmail.com':
        st.success ('email enviado com sucesso')
    else:
        st.error('email invalido')

#converter para inteiro

#import streamlit as st

# numero1=st.text_input('digite o numero')     
# numero2=st.text_input('digite o numero') 

# if st.button ('enviar'):
#resultado = int (numero 1) + int(numero 2)
#st.text(f' o resultado é {resultado}')


