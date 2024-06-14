import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_qrcode_scanner import qrcode_scanner

st.set_page_config(page_title="Billing", page_icon="be_favicon.png", initial_sidebar_state="collapsed", layout="wide")
st.image("bettr_earth_logo.png",width=140)

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

col1, col2 = st.columns(2)
with col1:
    st.write("This is col1")

with col2:
    product_code = qrcode_scanner()