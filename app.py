import os
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"  # Disable file watcher

import streamlit as st
from streamlit.components.v1 import declare_component

build_path = "./frontend/build"
if os.path.exists(build_path):
    st.write("[DEBUG] Build path exists. Proceeding to declare wallet_component.")
else:
    st.error("[DEBUG] Build path does not exist. Ensure the frontend is built and deployed correctly.")
    raise FileNotFoundError(f"[DEBUG] Build directory not found at {build_path}")

# Declare wallet component
try:
    wallet_component = declare_component("wallet_component", path=build_path)
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
