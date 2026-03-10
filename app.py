import streamlit as st

st.set_page_config(page_title="IFRS Explorer")

st.title("IFRS Explorer")

st.write("""
This application lists the IFRS Accounting Standards currently issued
by the International Accounting Standards Board (IASB).

Source:
https://www.ifrs.org/issued-standards/list-of-standards/
""")

# IFRS standards (2026)

ifrs_standards = [

"IFRS 1 – First-time Adoption of International Financial Reporting Standards",
"IFRS 2 – Share-based Payment",
"IFRS 3 – Business Combinations",
"IFRS 4 – Insurance Contracts",
"IFRS 5 – Non-current Assets Held for Sale and Discontinued Operations",
"IFRS 6 – Exploration for and Evaluation of Mineral Resources",
"IFRS 7 – Financial Instruments: Disclosures",
"IFRS 8 – Operating Segments",
"IFRS 9 – Financial Instruments",
"IFRS 10 – Consolidated Financial Statements",
"IFRS 11 – Joint Arrangements",
"IFRS 12 – Disclosure of Interests in Other Entities",
"IFRS 13 – Fair Value Measurement",
"IFRS 14 – Regulatory Deferral Accounts",
"IFRS 15 – Revenue from Contracts with Customers",
"IFRS 16 – Leases",
"IFRS 17 – Insurance Contracts",
"IFRS 18 – Presentation and Disclosure in Financial Statements",
"IFRS 19 – Subsidiaries without Public Accountability: Disclosures"

]

# Sidebar list

st.sidebar.title("IFRS Standards")

selected_standard = st.sidebar.selectbox(
"Select IFRS Standard",
ifrs_standards
)

# Main display

st.header(selected_standard)

st.write("""
A description of this standard can be added here in a future version of the
application.

This project demonstrates a Python Streamlit interface for navigating
IFRS Accounting Standards.
""")

st.caption(
"Source: IFRS Foundation – List of IFRS Accounting Standards"
)
