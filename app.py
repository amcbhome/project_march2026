import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config(page_title="IFRS Explorer")

SOURCE = "https://www.ifrs.org/issued-standards/list-of-standards/"

@st.cache_data
def get_ifrs_standards():

    try:

        r = requests.get(SOURCE, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        standards = []

        for tag in soup.find_all(["a","li","p"]):

            text = tag.get_text(strip=True)

            if re.match(r"IFRS\s\d+\s", text):

                standards.append(text)

        standards = sorted(set(standards))

        if len(standards) < 10:
            raise Exception("Parsing issue")

        return standards

    except:

        return ["Unable to retrieve IFRS standards"]


standards = get_ifrs_standards()


# Sidebar
st.sidebar.title("IFRS Standards")

selected = st.sidebar.selectbox(
"Select Standard",
standards
)


# Main page
st.title("IFRS Explorer")

st.header("Conceptual Framework")

st.write("""
The Conceptual Framework for Financial Reporting provides the
foundation for International Financial Reporting Standards.

It establishes the objective of financial reporting and the concepts
underlying the preparation and presentation of financial statements.

Key elements include:

• Objective of financial reporting  
• Qualitative characteristics of useful information  
• Definitions of assets, liabilities, income and expenses  
• Recognition and measurement principles  
• Presentation and disclosure
""")


st.header(selected)

st.subheader("Objective")

st.write("""
Each IFRS standard begins by stating the accounting issue the
standard intends to address and the objective of the reporting
requirements.
""")

st.subheader("Scope")

st.write("""
The scope identifies the transactions and entities to which the
standard applies and specifies any exclusions.
""")

st.subheader("Definitions")

st.write("""
Important technical terms are defined to ensure consistent
interpretation of the standard across reporting entities.
""")

st.subheader("Recognition")

st.write("""
Recognition rules determine when assets, liabilities, income
or expenses should be recognised in the financial statements.
""")

st.subheader("Measurement")

st.write("""
Measurement requirements specify how items should be valued,
including historical cost, fair value, or amortised cost.
""")

st.subheader("Presentation")

st.write("""
Presentation rules determine how information appears in the
financial statements.
""")

st.subheader("Disclosure")

st.write("""
Disclosure requirements ensure sufficient information is
provided in the notes to explain reported figures.
""")

st.caption("Source: IFRS Foundation – IFRS Accounting Standards")
