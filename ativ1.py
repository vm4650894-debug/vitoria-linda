import streamlit as st
lista=st.columns(4)

with lista[0]:
    st.write('coluna 1')
    numero1=st.text_input('digite o numero ')
    numero2=st.text_input('digite o numero  ')
    if st.button('somar'):
        resultado= int (numero1) + int (numero2)
        st.text(f' o resultado é {resultado}')

with lista[1]:
    st.write ('coluna 2')
    operaçao1=st.text_input('digite o numero´´')
    operaçao2=st.text_input('digite o numero')
    if st.button ('dividir'):
        resultado= int (operaçao1)/int(operaçao2)
        st.text(f' o resultado é {resultado}') 

with lista[2]:
    st.write('coluna 3')
    nu1=st.text_input('digite o num')
    nu2=st.text_input('digite o nume')
    if st.button ('subtrair'):
        resultado= int (nu1)-int(nu2)
        st.text(f' o resultado é {resultado}') 


with lista[3]:
    st.write('coluna 4')
    operador1=st.text_input('digite o operador')
    operador2=st.text_input('digite a operador''')
    if st.button ('multiplicar'):
        resultado= int (operador1)*int(operador2)
        st.text(f' o resultado é {resultado}') 
       
          