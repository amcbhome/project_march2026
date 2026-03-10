import streamlit as st
from database import get_standards, get_description

st.set_page_config(page_title="IFRS Explorer")

st.title("IFRS Explorer")
st.write("Select a standard to view its description.")

standards = get_standards()

options = [
    f"{code} – {title}"
    for code, title in standards
]

selection = st.selectbox("Choose IFRS Standard", options)

code = selection.split(" – ")[0]

description = get_description(code)

st.subheader(selection)
st.write(description)
