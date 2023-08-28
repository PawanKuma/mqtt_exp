import streamlit as st
import random, json
import time

import paho.mqtt.subscribe as subscribe


st.title("MQTT Server by ResoluteAI Software")

# Using object notation
vinworthjasaupur = st.sidebar.checkbox("vinworthjasaupur", value=True)
upapltest = st.sidebar.checkbox("upapltest", value=True)
vinworthtest = st.sidebar.checkbox("vinworthtest", value=True)

schemes = [vinworthjasaupur, upapltest, vinworthtest]
names = {"vinworthjasaupur": vinworthjasaupur, "upapltest": upapltest, "vinworthtest": vinworthtest}
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
    # print(list(names.keys()))
    msg = subscribe.simple(list(names.keys()), qos=0, msg_count=1, retained=True, hostname="20.235.93.174",port=1883, client_id="paho-sub", keepalive=1, will=None, auth={'username':"raiak", 'password':"RAIsw@2023"}, tls=None)
    topic = msg.topic
    if msg!=None and names[topic]:
        message = st.chat_message("assistant")
        if topic == "vinworthjasaupur" or topic== "vinworthtest":
                schemename = schemeids[topic]
        elif topic== "upapltest":
#                 # print((json.loads(msg.payload))['trig'])
                schemename = schemeids[str((json.loads(msg.payload))['trig'])]
        message.write("Topic Name -->  "+ msg.topic + " || msg Counter --> "+ str(counter))
        message.write("Scheme Name -->  " + schemename)
        message.write(json.loads(msg.payload))
        counter+=1
