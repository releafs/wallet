import streamlit as st
from streamlit.components.v1 import declare_component
wallet_component = declare_component('wallet_component', path='./frontend/build')
st.title('Wallet Connect Test')
wallet_address = wallet_component()
if wallet_address:
    st.success(f'Wallet Connected: {wallet_address}')
else:
    st.warning('Please connect your wallet.')
