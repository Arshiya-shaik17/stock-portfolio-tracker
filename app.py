

get_ipython().system('pip install streamlit yfinance pyngrok matplotlib pandas --quiet')

get_ipython().run_cell_magic('writefile', 'app.py', 'import streamlit as st\nimport yfinance as yf\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\nst.set_page_config(page_title="Stock Portfolio Tracker", layout="centered")\n\nst.title("📊 Stock Portfolio Tracker")\n\nst.markdown("Enter your stock symbols and the number of shares you own (e.g., `AAPL:5, TSLA:3`).")\n\nuser_input = st.text_input("Your Portfolio:", "")\n\nif user_input:\n    portfolio = {}\n    errors = []\n\n    for item in user_input.split(","):\n        try:\n            symbol, shares = item.strip().split(":")\n            shares = int(shares)\n            stock = yf.Ticker(symbol.strip())\n            price = stock.info.get("regularMarketPrice", 0)\n\n            if price == 0:\n                errors.append(symbol.strip().upper())\n                continue\n\n            value = round(price * shares, 2)\n            portfolio[symbol.strip().upper()] = {\n                "Shares": shares,\n                "Price (USD)": price,\n                "Value (USD)": value\n            }\n        except:\n            errors.append(item.strip())\n\n    if portfolio:\n        df = pd.DataFrame.from_dict(portfolio, orient=\'index\')\n        df[\'Symbol\'] = df.index\n        df.reset_index(drop=True, inplace=True)\n        total = df[\'Value (USD)\'].sum()\n\n        st.subheader("✅ Portfolio Summary")\n        st.dataframe(df)\n\n        st.success(f"💰 Total Portfolio Value: ${round(total, 2)}")\n\n        st.subheader("📈 Portfolio Chart")\n        plt.figure(figsize=(8, 5))\n        plt.bar(df[\'Symbol\'], df[\'Value (USD)\'], color=\'orange\')\n        plt.xlabel(\'Stock Symbol\')\n        plt.ylabel(\'Value in USD\')\n        plt.title(\'Stock Distribution\')\n        st.pyplot(plt)\n\n        # Download CSV\n        csv = df.to_csv(index=False).encode()\n        st.download_button("Download CSV", csv, "portfolio.csv", "text/csv")\n\n    if errors:\n        st.warning("Could not fetch data for: " + ", ".join(errors))\n')

from pyngrok import ngrok
import time

# Kill any existing Streamlit processes
get_ipython().system('pkill streamlit')

# Create tunnel
public_url = ngrok.connect(port=8501)
print("App is live at:", public_url)

# Wait 2 seconds then start Streamlit
time.sleep(2)
get_ipython().system('streamlit run app.py &> /dev/null &')

# Import pyngrok
from pyngrok import ngrok
import time

# Kill any existing streamlit processes
get_ipython().system('pkill -f streamlit')

# Connect to streamlit port using ngrok
public_url = ngrok.connect(port=8501)
print("✅ App is live at:", public_url)

# Wait a moment before launching
time.sleep(2)

# Launch Streamlit app
get_ipython().system('streamlit run app.py &>/dev/null &')

from pyngrok import ngrok
import time

get_ipython().system('pkill -f streamlit')

public_url = ngrok.connect(port=8501)
print("✅ Your app is live at:", public_url)

time.sleep(2)
get_ipython().system('streamlit run app.py &>/dev/null &')

get_ipython().system('ngrok config add-authtoken 2vI5GFZPaSyT08MupNye5bWw6qh_aPPyVQDakGTLZ2odKM24')

from pyngrok import ngrok
import time

get_ipython().system('pkill -f streamlit')

public_url = ngrok.connect(port=8501)
print("✅ Your app is live at:", public_url)

time.sleep(2)
get_ipython().system('streamlit run app.py &>/dev/null &')

from pyngrok import ngrok
import time

get_ipython().system('pkill -f streamlit')

public_url = ngrok.connect(port=8501)
print("✅ Your app is live at:", public_url)

time.sleep(2)
get_ipython().system('streamlit run app.py &>/dev/null &')

from pyngrok import ngrok
import time

# Kill existing Streamlit processes
get_ipython().system('pkill -f streamlit')

# Start Streamlit in the background
get_ipython().system('streamlit run app.py &>/dev/null &')

# Wait a moment for Streamlit to start
time.sleep(3)

# Create tunnel correctly (use `http` keyword instead of `port`)
public_url = ngrok.connect("http://localhost:8501")
print("✅ Your app is live at:", public_url)

