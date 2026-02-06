# Assignment 1 

This project compares data storage formats and analyzes stock market data using Python.

---

## Requirements

Make sure the following Python libraries are installed:

pandas
numpy
pyarrow
polars
scikit-learn
matplotlib
streamlit
Install them using:
pip install pandas numpy pyarrow polars scikit-learn matplotlib streamlit

---

## Part 1 – Storage Benchmark

1. Open the Jupyter Notebook.

2. Run all cells from top to bottom.

3. The notebook will:

     - Load the dataset

     - Create larger versions (10x and 100x)

     - Benchmark CSV vs Parquet (Snappy and ZSTD)

The final results are shown in the table results_all.

⚠ Do not upload the generated 10x and 100x files. They are created only for performance testing.
---

## Part 2 – Data Processing & Machine Learning

1. Run the cells that:
- Create technical indicators (SMA and RSI)
- Split the data into training and testing sets
- Train Linear Regression and Random Forest models

2. The notebook will display:
- Model performance metrics
- Comparison between Pandas and Polars performance

---

## Part 3 – Dashboard

How to Run the Dashboard

1. Open Terminal

2. Windows: Open Command Prompt or PowerShell

3. Navigate to the project folder
-  cd Desktop\Assignment1

4. Make sure this folder contains:
- dashboard.py
- all_stocks_5yr.csv
   
5. Run the dashboard
- python -m streamlit run dashboard.py

6. Open in browser
After running the command, the terminal will show:
Local URL: http://localhost:8501

7. Stop the dashboard
- Press:Ctrl + C

## What the Dashboard Shows:

The dashboard allows you to:

1. Select a stock ticker

2. View historical price trends

3. See summary statistics

4. Display recent rows of stock data

---

## Files Included

| File | Description |
|------|-------------|
| assignment1.ipynb | Main analysis and benchmarks |
| dashboard.py | Interactive dashboard |
| README.md | Project instructions |

---

## Summary

This project demonstrates that Parquet is more efficient than CSV, especially for large datasets. It also shows how technical indicators and machine learning models can be used to analyze stock prices and visualize them through an interactive dashboard.
