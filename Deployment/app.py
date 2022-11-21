import streamlit as st
from PIL import Image

st.title("About System")
st.write("Here, the system uses your likes in order to recommend you with things that you might like. It uses the information provided by you over the dropdown and the ones it is able to gather and then it shows recommendations according to that.")
Image= Image.open('pic.jpg')
st.image(Image)
st.header("Working :")
st.write("1. Type or Select a Music from Dropdown. ")
st.write("2. Click [Get Recommendations] Button.")
st.write("3. It will Recommend you Top 5 Music Tracks by-default or else you can also specify how many recommendations you want by using slider in the sidebar. ")
st.write("4. Click on URL of any Music Tracks, it will redirect you to preview of that song. ")
st.write("5. If you like that particular song then we also gave spotify link so that you can copy past it to the web browser.")
st.write("6. You can also have a look on (All Tracks) in the sidebar.")
st.success("Enjoy the Music of Your Choice.")
