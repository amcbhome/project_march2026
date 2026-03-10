import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="IFRS Explorer")

SOURCE_URL = "https://www.ifrs.org/issued-standards/list-of-standards/"


def fetch_ifrs_standards():

    try:

        response = requests.get(SOURCE_URL)
        soup = BeautifulSoup(response.text, "html.parser")

        standards = []

        # Find all links that contain IFRS standards
        links = soup.find_all("a")

        for link in links:

            text = link.get_text(strip=True)

            if text.startswith("IFRS"):
                standards.append(text)

        # Remove duplicates and sort
        standards = sorted(set(standards))

        return standards

    except:
        return ["Unable to retrieve standards from IFRS website"]


standards = fetch_ifrs_standards()


# Sidebar
st.sidebar.title("IFRS Standards")

selected = st.sidebar.selectbox(
    "Select a Standard",
    standards
)


# Main page
st.title("IFRS Explorer")

st.write(
"""
This application retrieves the current list of IFRS Accounting Standards
from the IFRS Foundation website and displays them for exploration.
"""
)

st.subheader(selected)

st.write(
"""
To view the full standard, consult the IFRS Foundation website.

Source:
https://www.ifrs.org/issued-standards/list-of-standards/
"""
)
