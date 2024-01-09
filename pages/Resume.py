import streamlit as st
import base64
from pathlib import Path

st.set_page_config(layout="wide")

content = "My Resume"

pdf_path = Path("pages/certificates /Resume_QA_Engineer_Dina_Butko.pdf")
base64_pdf = base64.b64encode(pdf_path.read_bytes()).decode("utf-8")

pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" width="800px" height="993px" type="application/pdf"></iframe>
"""
st.markdown(pdf_display, unsafe_allow_html=True)

with open("pages/certificates /Resume_QA_Engineer_Dina_Butko.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download CV",
                   data=PDFbyte,
                   file_name="Resume_QA_Engineer_Dina_Butko.pdf")
