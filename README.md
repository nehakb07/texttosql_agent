# AI Business Intelligence Agent

## Overview

The AI Agent is a prototype analytics system that automatically cleans structured business data and enables natural language querying using an Text-to-SQL AI agent.

The goal of this project is to demonstrate how non-technical users can analyze enterprise datasets without writing SQL, while ensuring data quality through an built-in cleaning pipeline.

This project simulates a sellable AI analytics product that combines automated data preparation with AI-driven insights.

---

## Problem Statement

Business teams often struggle to extract insights from structured datasets because:

* Raw data contains inconsistent formats and missing values
* Writing SQL requires technical expertise
* Data cleaning is time-consuming
* Analysts spend significant effort preparing data instead of generating insights

This project addresses these challenges by automating data cleaning and enabling natural language analytics.

---

## Solution

The system includes two core agents:

1. **Data Cleaning Agent**

   * Removes duplicates
   * Standardizes numeric and date formats
   * Handles missing values
   * Produces a clean dataset for analysis

2. **Text-to-SQL Agent**

   * Converts natural language questions into SQL
   * Executes queries using DuckDB
   * Returns structured insights and visualizations

Users can ask business questions in plain English and receive analytical results instantly.

---

## Architecture

```
Raw CSV Data
    ↓
Data Cleaning Agent
    ↓
Typed DataFrame
    ↓
Text-to-SQL AI Agent
    ↓
DuckDB Query Execution
    ↓
Visualization Dashboard
```

The modular architecture allows easy extension to additional agents such as document intelligence or forecasting systems.

---

## Features

* Automated data cleaning pipeline
* Natural language to SQL conversion
* Real-time analytics execution
* Interactive dashboard visualization
* Error-resilient query handling
* Modular agent architecture

---

## Example Questions

### Basic Aggregations

* Show total revenue by region
* Show total profit by country
* Show total units sold by item type
* What is the average unit price by item type
* Show total sales by sales channel

### Ranking and Top Performers

* Top 5 countries by total revenue
* Top 5 item types by total profit
* Which region has the highest total revenue
* Which country has the lowest total profit
* Top 10 orders by total revenue

### Comparative Analysis

* Compare online vs offline total revenue
* Compare total profit by region
* Show revenue and profit by item type
* Which sales channel performs better in total revenue
* Compare average unit price across regions

### Filtering and Conditions

* Show total revenue for orders after 2015
* Show total profit where units sold are greater than 5000
* Top profitable items in Asia
* Show orders with total revenue above 1,000,000
* Show total revenue for high priority orders

### Time-Based Analysis

* Show total revenue by year
* Show monthly revenue trends
* Compare yearly profit totals
* Show number of orders per year
* Show revenue growth over time

---

## Installation

### 1. Clone the repository

```
git clone <repository-url>
cd ai_business_agent
```

### 2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add API key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## Running the Application

```
streamlit run app.py
```

The dashboard will open in your browser where you can ask business questions about the dataset.

---

## Tech Stack

* Python
* Streamlit
* Pandas
* DuckDB
* Groq LLM API
* Modular agent architecture

---

## Future Enhancements

* Document intelligence (RAG agent)
* Predictive analytics and forecasting
* Advanced charting and dashboards
* Automated data quality reporting
* Multi-dataset support

## Output

<img width="1266" height="710" alt="Screenshot 2026-02-12 210415" src="https://github.com/user-attachments/assets/fee3e2b5-5e46-4875-9acf-eabb280f166d" />
<img width="1277" height="322" alt="Screenshot 2026-02-12 210510" src="https://github.com/user-attachments/assets/b09f8791-f30f-4558-b973-696ca6605fd5" />
<img width="1169" height="843" alt="Screenshot 2026-02-12 210502" src="https://github.com/user-attachments/assets/8eb3f1f6-5ca4-4c09-8df5-79634a670629" />
<img width="1239" height="327" alt="Screenshot 2026-02-12 210422" src="https://github.com/user-attachments/assets/abf0a240-dc61-4306-9e5a-2084604bf140" />

---

## Conclusion

This project demonstrates how AI agents can bridge the gap between raw enterprise data and actionable business insights. By combining automated data cleaning with natural language analytics, organizations can significantly reduce the time required to generate decisions from data.
