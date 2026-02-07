import streamlit as st
import pandas as pd
from agents.sql_agent import run_sql_agent
from utils.helpers import clean_sales_data

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Business Intelligence Agent",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("AI Business Intelligence Agent")

st.markdown("""
This system automatically cleans business data and enables natural language analytics 
using an Text-to-SQL AI agent.
""")

st.caption("Powered by automated data cleaning and AI-driven analytics")

# -----------------------------
# Layout
# -----------------------------
col1, col2 = st.columns([1, 2])

# -----------------------------
# Left Panel — Input + Pipeline
# -----------------------------
with col1:

    st.header("Ask a Business Question")

    question = st.text_area(
        "Enter your question:",
        placeholder="Example: Show total revenue by region"
    )

    run = st.button("Run Analysis")

    st.divider()

    st.subheader("Data Pipeline Status")

    if run:
        st.info("Running automated data cleaning pipeline...")

        cleaned_df = clean_sales_data()

        st.success("Data cleaning completed")

        st.write("Dataset summary:")
        st.write(f"Rows: {len(cleaned_df)}")
        st.write(f"Columns: {len(cleaned_df.columns)}")
        st.write(f"Missing values: {cleaned_df.isna().sum().sum()}")

# -----------------------------
# Right Panel — Results
# -----------------------------
with col2:

    st.header("Results")

    if run and question:

        sql, result = run_sql_agent(question)

        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        st.subheader("Query Output")

        if isinstance(result, str):
            st.error(result)

        else:
            st.dataframe(result, width="stretch")

            # Safe chart rendering
            try:
                numeric_cols = result.select_dtypes(include="number")

                if not numeric_cols.empty:
                    st.subheader("Visualization")
                    st.bar_chart(numeric_cols)

            except Exception:
                pass

    elif run and not question:
        st.warning("Please enter a question to analyze the data.")
