import streamlit as st
import streamlit_authenticator as stauth
import yaml
import random
import time
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
# List of four sample grocery items
sampleItems = {
    147121269830: "Cheese",
    147121269831: "Pork", 
    147121269832: "Chicken",
    147121269833: "Beans",
    147121269834: "Milk"
}

# https://github.com/michaeldwu/Foodprint-Calculator/blob/master/scripts/main.js

itemImpact = {
    # Carbon, Nitrogen, Water, Coin Value, Impact
    147121269830: [0.56, 5.32, 165, 5, 50],
    147121269831: [0.587, 11.3, 238, 8, 66], 
    147121269832: [0.434, 9.93, 128, 4, 68],
    147121269833: [0.034, 0.251, 72.5, 4, 33],
    147121269834: [0.31, 4.70, 168, 5, 45]
}
coinInc = 5
global coinVal 
impactParams = ["Low Impact", "Average", "High Impact"]

def envImpact(item):

    impactVal = (itemImpact[item][4])

    progress_text = "Impact Meter"
    my_bar = st.progress(0, text=progress_text)

    if impactVal >= 60:
        progress_text = "High Impact"
    elif impactVal <= 40:
        progress_text = "Low Impact"
    else:
        progress_text= "Average Impact"

    for percent_complete in range(impactVal):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)

    # Per servings of food
    f"Carbon Footprint: {itemImpact[item][0]} kg"              # kg of Carbon
    f"Nitrogen Footprint: {itemImpact[item][1]} g"              # g of Nitrogen lost
    f"Water Footprint:  {itemImpact[item][2]} L"               # L of Water consumed

    return progress_text


def rewardSystem(item):
    
    coinInc = itemImpact[item][3]
    randVal = random.randrange(10, 50)  
    coinMeter.metric(label="Rewards", value=randVal, delta=coinInc)
    
    # return

def recommendationSystem():
    
    lft, mid, rght = st.columns(3)
    lft.image("./alternatives/pork/jackfruit.png", caption="Jackfruit")
    mid.image("./alternatives/pork/shredded_seitan.png", caption="Shredded Seitan")
    rght.image("./alternatives/pork/chanterelle_mushrooms.png", caption="Chanterelle Mushrooms")
    

col1, col2 = st.columns(2)
with col2:
    st.write("This is col2")
    # product_code = qrcode_scanner()
    product_code = 147121269830
    

with col1:
    st.subheader(f"Environment Impact of {sampleItems[product_code]}")
    # envHeader = st.subheader("Environmental Impact Calculator")
    st.divider()
    impact = envImpact(product_code)
    st.divider()
    if impact == "Low Impact" or impact == "Average Impact":
        st.subheader("BE Coins :coin:")
        coinVal=11
        coinMeter = st.metric(label="Rewards", value=11, delta=coinInc)
        rewardSystem(product_code)
        
        
    else:
        st.subheader("Bettr Alternatives")
        recommendationSystem()


    
