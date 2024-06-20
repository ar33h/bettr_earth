# Visa Hackathon 2024
# Challenge 1: Groceries for Good
# Team Pace University - Arshdeep, Jasmeet

# Mobile App for Customers

# Modules
import streamlit as st
import streamlit_authenticator as stauth
import yaml
import cv2
from yaml.loader import SafeLoader
from streamlit_qrcode_scanner import qrcode_scanner

st.set_page_config(page_title="Bettr Earth", page_icon="be_favicon.png", initial_sidebar_state="collapsed")
st.image("./splash.png")

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

login_col, register_col = st.columns(2)
with login_col:
    st.write('')
    warnmsg = st.warning('Login for a sustainable shopping experience')
    status = authenticator.login(
        max_login_attempts=3,
        fields={'Form name':'Login', 'Username':'Email', 'Password':'Password'}
    )
    
    forgotPass = st.markdown('')
    forgotPass.markdown('<a href="" target="_self">Forgot Password?</a>', unsafe_allow_html=True)
    # def forgot():
    #     try:
    #         if authenticator.reset_password(st.session_state["username"]):
    #             st.success('Password modified successfully')
    #     except Exception as e:
    #         st.error(e)
    
    if st.session_state["authentication_status"]:
    # customerCheckin()
        st.markdown('<a href="items" target="_self">Scan an Item</a>', unsafe_allow_html=True)
        forgotPass.markdown('<a href="" target="_self">Change Password?</a>', unsafe_allow_html=True)
        warnmsg.warning(f'Welcome {st.session_state["name"]}')
        authenticator.logout()
    
    # st.write(f'Ready to  *{st.session_state["name"]}*')
    # authenticator.logout()
    elif st.session_state["authentication_status"] is False:
        st.error('Employee ID and/or Password is Incorrect!')
    # elif st.session_state["authentication_status"] is None:
    #     st.warning('Login for a sustainable shopping experience')

with register_col:
    # try:
    registeration = authenticator.register_user(
        
        
        fields={'Form name':'New here?', 'Email':'Email', 'Username':'Username', 'Password':'Password', 'Repeat password':'Repeat password', 'Register':'Register'},
        pre_authorization=False,
        
    )
    #     if registeration:
    #         st.success('User registered successfully')
    # except Exception as e:
    #     st.error(e)

# st.markdown("""
#     <style>
#         [data-testid="column"]:nth-child(2){
            
#             background-color: #15A06E;
#         }
#     </style>
#     """, unsafe_allow_html=True
# )
# st.text(status)


