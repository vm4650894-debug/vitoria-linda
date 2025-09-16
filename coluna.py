import streamlit as st
st.sidebar.image('gatos.jpg')
st.sidebar. title('calculo de IMC')

conls = st.columns(2)
conls[0].write('👌coluna 1')
conls[1].write('😂coluna 2')
conls[2].write('😒coluna 3')
conls[3].write('🤷‍♀️coluna 4')


if st.button('meu botao'):
    st.write('voce clicou forte demais')

