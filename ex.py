import streamlit as st
con=st.columns(4)

with con[0]:
    st.write('coluna 1')
    st.button('clique aqui')

with con[1]:
    st.write ('coluna 2')
    st.button('clique aqui')

with con[2]:
    st.write('coluna 3') 
    st.button('clique aqui') 

with con[3]:
    st.write('coluna 4')
    st.button ('clique aqui')
