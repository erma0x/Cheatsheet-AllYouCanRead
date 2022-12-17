#test_steamlit
import pandas as pd
import streamlit as st

st.write("""
# My first app
Hello world!

""")
df = pd.read_csv("data.csv")
st.line_chart(df)
