import streamlit as st
st.title("Ejemplo para usar session_state")

if 'count' not in st.session_state:
    st.session_state['count'] = 0

if st.button('Click me'):
    st.session_state['Count'] += 1


st.write(st.session_state)
