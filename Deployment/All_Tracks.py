import streamlit as st
import pandas as pd
import pickle

#Loading all the tracks  
music = pickle.load(open('music.pkl', 'rb'))
musicdf = pd.DataFrame(music)
st.title("All Tracks ")
st.dataframe(musicdf, 3000, 500)
