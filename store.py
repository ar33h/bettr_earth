import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_qrcode_scanner import qrcode_scanner

st.set_page_config(page_title="My Store", page_icon="be_favicon.png", initial_sidebar_state="collapsed")
st.image("splash.png")

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

status = authenticator.login(
    max_login_attempts=3,
    fields={'Form name':'System Login', 'Username':'Employee ID', 'Password':'Password'}
)

# st.text(status)

def customerCheckin():
    beCustomers = {185263954497: "Harry", 185263954498: "Ron", 185263954499: "Hermione"}

    msg = st.warning('Scan Member Code to Start!')
    nextBtn = st.markdown('')
    # bar_code = qrcode_scanner()
    # qr_code = 1 
    # st.write(qr_code)
    bar_code = 185263954497
    # customerName = ""
    
    if bar_code == 185263954497:
        customerName = beCustomers[185263954497]
        
    elif bar_code == 185263954498:
        customerName = beCustomers[185263954498]

    elif bar_code == 185263954499:
        customerName = beCustomers[185263954499]
    
    else:
        msg.error("Invalid Code. Member does not exist")
        return

    msg.success(f'Hello {customerName}')
    nextBtn.markdown('<a href="items" target="_self">Start Billing</a>', unsafe_allow_html=True)
        # if st.button(label="Start"):
    
# def itemCheckout():
    
if st.session_state["authentication_status"]:
    customerCheckin()
    
    # st.write(f'Ready to  *{st.session_state["name"]}*')
    # authenticator.logout()

elif st.session_state["authentication_status"] is False:
    st.error('Employee ID and/or Password is Incorrect!')
elif st.session_state["authentication_status"] is None:
    st.warning('Login to start billing greener choices')

