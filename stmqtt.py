import streamlit as st
import random, json
import time

import paho.mqtt.subscribe as subscribe


st.title("Simple MQTT Server")

# Using object notation
vinworthjasaupur = st.sidebar.checkbox("vinworthjasaupur")
upapltest = st.sidebar.checkbox("upapltest")
vinworthtest = st.sidebar.checkbox("vinworthtest")

schemes = [vinworthjasaupur, upapltest, vinworthtest]
names = ["vinworthjasaupur", "upapltest", "vinworthtest"]
schemeids = {"vinworthtest":"Bulandshahar - Alampur nagla", "vinworthjasaupur": "Jaunpur (Jasaupur)", "861190059947132":"Sant Ravidas Nagar - Jethupur", "861190059974243":"Ambedkar Nagar- Rukunpur kasimpur","861198066252826": "Amethi- sogara"}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


counter = 1
while True:
    msg = subscribe.simple(list(names.keys()), qos=0, msg_count=1, retained=True, hostname="20.235.93.174",port=1883, client_id="paho-sub", keepalive=1, will=None, auth={'username':"raiak", 'password':"RAIsw@2023"}, tls=None)
    if msg!=None and names[msg.topic]:
        message = st.chat_message("assistant")
        message.write("Topic Name -->  "+ msg.topic + "  msg Counter --> "+ str(counter))
        message.write("Scheme Name -->  " + schemeids[msg.topic])
        message.write(json.loads(msg.payload))
        counter+=1
