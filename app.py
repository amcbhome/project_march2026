import streamlit as st

st.set_page_config(page_title="IFRS Explorer")

st.title("IFRS Explorer")
st.write("Browse the IFRS framework as a series of chapters.")

chapters = {

"Chapter 1 — Introduction to IFRS":
{
"description":
"""
This chapter introduces International Financial Reporting Standards (IFRS)
and explains their purpose within global financial reporting. IFRS provides
a common accounting language that improves comparability of financial
statements across countries and industries.

It also explains the role of the International Accounting Standards Board
(IASB), which is responsible for issuing IFRS standards.
""",

"background":
"""
IFRS evolved from earlier International Accounting Standards (IAS)
developed by the International Accounting Standards Committee (IASC)
from 1973 onwards. In 2001 the IASB replaced the IASC and began issuing
IFRS standards.
""",

"chapter_count": "Approx. 14–20 introductory sections depending on textbook",
"word_count": "Approx. 3,000–5,000 words in most IFRS textbooks",

"source":
"""
IFRS Foundation (2023). International Financial Reporting Standards.
Conceptual Framework for Financial Reporting.
https://www.ifrs.org
"""
},

"Chapter 2 — Conceptual Framework":
{
"description":
"""
This chapter explains the IFRS Conceptual Framework which underpins all
financial reporting standards.

The framework defines:

• the objective of financial reporting  
• qualitative characteristics of useful information  
• definitions of assets, liabilities, equity, income and expenses  
• recognition and measurement principles.
""",

"background":
"""
The Conceptual Framework was originally developed in the 1980s and
has been revised several times, most recently in 2018.

It provides theoretical guidance for standard-setting and helps ensure
consistency across IFRS standards.
""",

"chapter_count": "Approximately 8 major sections",
"word_count": "Approx. 8,000 words in official IASB documentation",

"source":
"""
IFRS Foundation (2018). Conceptual Framework for Financial Reporting.
"""
},

"Chapter 3 — Presentation of Financial Statements":
{
"description":
"""
This chapter describes how financial statements are structured under IFRS.

Entities must present:

• Statement of Financial Position  
• Statement of Profit or Loss and Other Comprehensive Income  
• Statement of Changes in Equity  
• Statement of Cash Flows  
• Notes to the financial statements.
""",

"background":
"""
The principles largely originate from IAS 1, one of the oldest
international accounting standards still in force.

It establishes minimum presentation requirements and ensures
comparability across reporting entities.
""",

"chapter_count": "10–15 sections depending on source",
"word_count": "Approx. 6,000–9,000 words",

"source":
"""
IAS 1 Presentation of Financial Statements.
IFRS Foundation.
"""
},

"Chapter 4 — Measurement and Valuation":
{
"description":
"""
This chapter explains how assets and liabilities are measured in IFRS.

Common measurement bases include:

• historical cost  
• fair value  
• value in use  
• amortised cost.

Different standards apply different measurement approaches
depending on the economic substance of the transaction.
""",

"background":
"""
Measurement is one of the most debated topics in accounting.
Modern IFRS increasingly emphasises fair value measurement,
particularly in financial instruments and investment assets.
""",

"chapter_count": "Approx. 12 sections",
"word_count": "Approx. 5,000–8,000 words",

"source":
"""
IFRS 13 Fair Value Measurement.
IFRS Conceptual Framework.
"""
},

"Chapter 5 — Revenue Recognition":
{
"description":
"""
This chapter explains how revenue is recognised under IFRS.

The core principle is that revenue should reflect the transfer
of promised goods or services to customers in an amount that
reflects the consideration expected.

This concept is implemented through the five-step model.
""",

"background":
"""
Revenue accounting was historically inconsistent across industries.
IFRS 15 unified previous standards and introduced a consistent
principle-based model.
""",

"chapter_count": "Approx. 5 core stages",
"word_count": "Approx. 10,000+ words in full IFRS guidance",

"source":
"""
IFRS 15 Revenue from Contracts with Customers.
IFRS Foundation.
"""
},

"Chapter 6 — Financial Instruments":
{
"description":
"""
This chapter explains accounting for financial assets and liabilities.

Key topics include:

• classification and measurement  
• impairment using expected credit loss models  
• hedge accounting.
""",

"background":
"""
IFRS 9 replaced IAS 39 following criticism of the earlier model
during the global financial crisis.

The new expected credit loss model requires earlier recognition
of credit losses.
""",

"chapter_count": "Approx. 20 sections",
"word_count": "Over 15,000 words in the official standard",

"source":
"""
IFRS 9 Financial Instruments.
IFRS Foundation.
"""
},

"Chapter 7 — Leases":
{
"description":
"""
This chapter explains lease accounting.

Under IFRS 16, most leases must be recognised on the balance sheet
by recording:

• a right-of-use asset  
• a lease liability.
""",

"background":
"""
IFRS 16 replaced IAS 17 and eliminated many off-balance-sheet
leases, improving transparency for investors.
""",

"chapter_count": "Approx. 12 sections",
"word_count": "Approx. 8,000 words",

"source":
"""
IFRS 16 Leases.
IFRS Foundation.
"""
}

}

chapter = st.selectbox(
"Select Chapter",
list(chapters.keys())
)

data = chapters[chapter]

st.header(chapter)

st.subheader("Description")
st.write(data["description"])

st.subheader("Background")
st.write(data["background"])

st.subheader("Approximate Structure")
st.write("Sections:", data["chapter_count"])
st.write("Estimated word count:", data["word_count"])

st.subheader("Source")
st.write(data["source"])
