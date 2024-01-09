import streamlit as st

st.set_page_config(layout="wide")

content = "My Certificates"

st.title(content)
col1, empty_column, col2 = st.columns([1.5, 0.5, 1.5])

images = "pages/certificates"

with col1:
        st.image("pages/certificates /ISTQB Dzina Butko.png", width=600)
        st.image("pages/certificates /img.png", width=600)
        st.image("pages/certificates /img_1.png", width=600)
        st.image("pages/certificates /img_2.png", width=600)
