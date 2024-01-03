import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Dina Butko")
    content = """
    Hi, i am Dina! I am QA Engineer. 
    """
    st.write(content)
