import streamlit as st
st.sidebar.image('gatos.jpg')
st.sidebar. title('calculo de IMC')

conls = st.columns(2)
conls[0].write('👌coluna 1')
conls[1].write('😂coluna 2')

if st.button ('meu amor'):
    st.write ('nao te amo mais')
    