import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.title("📈 Stock Price Dashboard (Simple)")

DATA_PATH = "all_stocks_5yr.csv"

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # делаем названия колонок безопасными
    df.columns = df.columns.str.strip().str.lower()

    # проверка обязательных колонок
    required = {"date", "name", "close", "volume"}
    missing = required - set(df.columns)
    if missing:
        st.error(f"Missing columns in CSV: {missing}")
        st.write("Columns found:", list(df.columns))
        st.stop()

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["name", "date"])
    return df

df = load_data(DATA_PATH)

# Sidebar filters
st.sidebar.header("Filters")
tickers = sorted(df["name"].unique())
ticker = st.sidebar.selectbox("Select stock (ticker)", tickers)

df_stock = df[df["name"] == ticker].copy().sort_values("date")

st.subheader(f"Selected: {ticker}")
c1, c2, c3 = st.columns(3)
c1.metric("Rows", f"{len(df_stock):,}")
c2.metric("Date range", f"{df_stock['date'].min().date()} → {df_stock['date'].max().date()}")
c3.metric("Last close", f"{df_stock['close'].iloc[-1]:.2f}")

# Plot
st.subheader("Close Price over Time")
fig = plt.figure(figsize=(12, 4))
plt.plot(df_stock["date"], df_stock["close"])
plt.xlabel("Date")
plt.ylabel("Close")
plt.tight_layout()
st.pyplot(fig)

# Table
st.subheader("Last 20 rows")
st.dataframe(df_stock.tail(20), use_container_width=True)

# Simple stats
st.subheader("Basic Statistics")
stats = df_stock[["close", "volume"]].describe()
st.dataframe(stats, use_container_width=True)
