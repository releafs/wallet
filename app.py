import os
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"  # Disable file watcher

import streamlit as st
from streamlit.components.v1 import declare_component

# Declare wallet component
st.write("[DEBUG] Starting Streamlit app...")
try:
    wallet_component = declare_component("wallet_component", path="./frontend/build")
    st.write("[DEBUG] Wallet component declared successfully.")
except Exception as e:
    st.error(f"[DEBUG] Failed to declare wallet component: {e}")
    raise

st.title("Wallet Connect Test")
wallet_address = wallet_component()
if wallet_address:
    st.success(f"[DEBUG] Wallet Connected: {wallet_address}")
else:
    st.warning("[DEBUG] Please connect your wallet.")
