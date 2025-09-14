import streamlit as st
import pandas as pd
import helper

st.title("Financial Data Extraction Tool")
financial_data_df = pd.DataFrame({
    "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "Total Assets", "EBITDA", "Stock Price", "EPS"],
    "Value": ["", "", "", "", "", "", "", ""]
})

col1, col2 = st.columns([3, 2])

with col1:
    st.header("Extractor Tool")
    article_text = st.text_area("Enter financial text(article) here:", height=350)
    if st.button("Extract"):
        financial_data_df = helper.extract_financial_info(article_text)

with col2:
    # st.header("Resultant Dataframe")
    st.markdown("<br>" * 3, unsafe_allow_html=True)
    st.dataframe(
        financial_data_df,
        column_config = {
            "Measure": st.column_config.Column(width=150),
            "Value": st.column_config.Column(width=150)
        },
        hide_index=True
    )