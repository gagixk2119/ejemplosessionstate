import streamlit as st
st.title("Ejemplo para usar session_state")

if "count" not in st.session_state:
    st.session_state["count"] = 0


st.write(st.session_state)
