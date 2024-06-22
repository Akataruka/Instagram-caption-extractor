import utils
import streamlit as st 


st.title(":red[Instagram-Caption-Extractor] :sunglasses:")
st.markdown("### Enter the Instagram Post URL below:")
url = st.text_input("URL",placeholder="Enter the URL here")
c1,c2,c3 = st.columns([2,1,2])
with c2:
    sub = st.button("Submit")
if sub:
    caption = utils.get_instagram_caption(url)
    st.write("The caption is:")
    st.code(caption,language="markdown")
    