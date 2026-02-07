import pandas as pd
import duckdb
import os
from dotenv import load_dotenv
from groq import Groq
from utils.helpers import clean_sales_data

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_data():

    df = clean_sales_data()
    duckdb.register("sales", df)

    return df

def generate_sql(question, schema):

    prompt = f"""
You are an DuckDB SQL expert.

Table name: sales

IMPORTANT RULES:
- Column names contain spaces.
- ALWAYS wrap column names in double quotes.
- Use exact column names from the list below.
- Do NOT invent new column names.
- Always use clear column aliases with AS

Columns:
{schema}

Return ONLY valid DuckDB SQL.

Question: {question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    sql = response.choices[0].message.content

    # Clean SQL output
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql


def run_sql_agent(question):

    df = load_data()
    schema = "\n".join(df.columns)

    sql_query = generate_sql(question, schema)

    try:
        result = duckdb.query(sql_query).to_df()
    except Exception as e:
        return sql_query, f"SQL Error: {e}"

    return sql_query, result
