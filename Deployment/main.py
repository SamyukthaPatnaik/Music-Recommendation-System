import streamlit as st
import pickle
import pandas as pd
import webbrowser
from streamlit_option_menu import option_menu
# import link_button
# import HYPERLINK
st.set_page_config(layout="wide")
st.sidebar.title("MENU")
no_recommend = st.sidebar.slider ( 'How many Recommendations you want?', 5, 20, 5)
st.sidebar.write ( "I want ", no_recommend, 'Recommendations' )
def recommend(musics):
    Index = music[music['Track_Name'] == musics].index[0]
    distances = sorted(list(enumerate(similarity[Index])), reverse=True, key=lambda x: x[1])
    # no_recommend = int(input("How many recommandations you want? "))

    recommended_music_names = []
    for i in distances [0:no_recommend]:
       recommended_music_names.append(music.iloc[i[0]].Track_Name)
    return recommended_music_names

with st.sidebar:
    choice = option_menu ( menu_title=None,
                           options=["Recommendation","About System", "All Tracks"],
                           icons=["bookmark-check-fill","info-circle", "music-note-list"],
                           default_index=0)
if choice == "Recommendation":
    st.title( " MUSIC RECOMMENDATION SYSTEM" )
    st.write('MEDITATION  &  RELAXATION')
    music = pickle.load(open('music.pkl', 'rb'))
    musicdf= pd.DataFrame(music)
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    music_list = musicdf['Track_Name'].values
    selected_music_name = st.selectbox("Search Music : Type or Select a Music from the Dropdown", music_list)


    if st.button('Get Recommendations'):
        recommendations = recommend(selected_music_name)
        col1, col2, col3 = st.columns ( 3 )
        with col1:
            st.subheader( "Track Names" )
        with col2:
            st.subheader( 'Track URL' )
        with col3:
            st.subheader( "Preview Link" )
        for i in recommendations:
            index_no = (musicdf [musicdf ["Track_Name"] == i].index [0]) #location access in url of each song
            preview_link = musicdf["Track_Preview"][index_no]
            # st.write(i, "  -----  ", (musicdf ['Track_URI'] [index_no]), "-----", preview_link)

            col1, col2, col3 = st.columns (3)
            with col1:
                st.write(i)
            with col2:
                st.write(musicdf ['Track_URI'] [index_no])
            with col3:
                st.write(preview_link)

    else:
        st.write('Click [Get Recommendations] Button ')



# with st.sidebar:
#     choice = option_menu(menu_title=None,
#                          options=["About System", "All Tracks"],
#                          icons=["info-circle", "music-note-list"])
if choice == 'About System':
    about = 'http://localhost:8502'
    webbrowser.open_new_tab(about)
if choice == 'All Tracks':
    All_Tracks = 'http://localhost:8503'
    webbrowser.open_new_tab(All_Tracks)


