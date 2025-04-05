import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Portfolio Tracker", layout="centered")

st.title("📊 Stock Portfolio Tracker")

st.markdown("Enter your stock symbols and the number of shares you own (e.g., `AAPL:5, TSLA:3`).")

user_input = st.text_input("Your Portfolio:", "")

if user_input:
    portfolio = {}
    errors = []

    for item in user_input.split(","):
        try:
            symbol, shares = item.strip().split(":")
            shares = int(shares)
            stock = yf.Ticker(symbol.strip())
            price = stock.info.get("regularMarketPrice", 0)

            if price == 0:
                errors.append(symbol.strip().upper())
                continue

            value = round(price * shares, 2)
            portfolio[symbol.strip().upper()] = {
                "Shares": shares,
                "Price (USD)": price,
                "Value (USD)": value
            }
        except:
            errors.append(item.strip())

    if portfolio:
        df = pd.DataFrame.from_dict(portfolio, orient='index')
        df['Symbol'] = df.index
        df.reset_index(drop=True, inplace=True)
        total = df['Value (USD)'].sum()

        st.subheader("✅ Portfolio Summary")
        st.dataframe(df)

        st.success(f"💰 Total Portfolio Value: ${round(total, 2)}")

        st.subheader("📈 Portfolio Chart")
        plt.figure(figsize=(8, 5))
        plt.bar(df['Symbol'], df['Value (USD)'], color='orange')
        plt.xlabel('Stock Symbol')
        plt.ylabel('Value in USD')
        plt.title('Stock Distribution')
        st.pyplot(plt)

        # Download CSV
        csv = df.to_csv(index=False).encode()
        st.download_button("Download CSV", csv, "portfolio.csv", "text/csv")

    if errors:
        st.warning("Could not fetch data for: " + ", ".join(errors))
