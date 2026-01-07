import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #f4dcbb;
    color: #f4dcbb;
}

div[data-testid="column"] {
    background-color: #2a2a2a;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 12px;
}

/* Headers */
h1, h2, h3, h4 {
    color: #f1f1f1;
}

/* Buttons */
.stButton > button {
    background-color: #4da3ff;
    color: white;
    border-radius: 8px;
    border: none;
}

/* Progress bar */
div[data-testid="stProgress"] > div > div {
    background-color: #2ecc71;
}
</style>
""", unsafe_allow_html=True)
