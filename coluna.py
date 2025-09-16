import streamlit as st
lista=st.columns(4)



lista[0].write('👌coluna 1')
lista[1].write('😂coluna 2')
lista[0].write('😒coluna 3')
lista[1].write('🤷‍♀️coluna 4')


if lista[1].button('meu botao'):
    st.write('Você clicou forte demais')

