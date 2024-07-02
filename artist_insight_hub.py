import streamlit as st
import spotify_api
import pandas as pd
import time

st.set_page_config(page_title="Spotify Query using API",layout='wide',initial_sidebar_state='collapsed')
st.title('Artist Insight Hub')
artist_name = st.text_input('Provide name of the artist')
if len(artist_name)>0:
    with st.spinner('Please wait :stopwatch:'):
        time.sleep(2)
    artist_top_songs = []
    track_popularity = []
    preview_song = []
    top_songs = spotify_api.artist_top_tracks(artist_name)
    for song in top_songs:
        artist_top_songs.append(song['name'])
        track_popularity.append(song['popularity'])
        preview_song.append(song['preview_url'])
    df = pd.DataFrame({'Tracks': artist_top_songs,'Popularity': track_popularity})
    
    col1, col2, col3 = st.columns([2,3,5])

    with col1:
        st.title(spotify_api.get_artist_name(artist_name))
        st.image(spotify_api.get_artist_image(artist_name))


    with col2:
        genre_df = pd.DataFrame({'Genres': spotify_api.get_artist_genre(artist_name)})
        st.metric(label = 'Popularity', value = spotify_api.get_artist_popularity(artist_name), help = "The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.")
        st.dataframe(genre_df, hide_index = True)

    with col3:
        st.subheader("Artist's top tracks")
        st.data_editor(
        df,
        column_config={
            "Popularity":st.column_config.ProgressColumn(
                'Popularity',
                help = 'Popularity of the song',
                min_value = 0,
                max_value = 100,
                width = "medium"
            ),
        },hide_index = True,use_container_width =True)

    with st.container(border=True):
        st.header('Song Preview')
        selected_song = st.radio('Select the song to preview',artist_top_songs)
        index = artist_top_songs.index(selected_song)
        
        if selected_song:
            if preview_song[index] is None:
                st.error('No preview available for this song')
            else:
                st.markdown(f"Preview link : [{preview_song[index]}]({preview_song[index]})")
                st.audio(preview_song[index], format='audio/mp3')

else:
    st.warning('Please provide Artist name')