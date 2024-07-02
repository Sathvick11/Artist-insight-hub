#AUTHOR : Sathvick Bindinganavale Srinath
#USAGE : The programs retrieves data from Spotify using the API and queries it using streamlit.

import streamlit as st
import pandas as pd
import requests
import json
import base64

CLIENT_ID = st.secrets['CLIENT_ID']
CLIENT_SECRET = st.secrets['CLIENT_SECRET']
AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

def get_access_token():
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token

headers = {
    'Authorization': 'Bearer {token}'.format(token=get_access_token()),
    "Content-Type": "application/json"
}

@st.cache_data
def get_artist_id(artist_name):
    url = BASE_URL + 'search'
    search_filter = f'?q={artist_name}&type=artist&limit=1'
    query_url = url + search_filter
    result = requests.get(query_url,headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    result_ = json_result[0]
    result = result_['id'] 
    return result

@st.cache_data
def get_artist_image(artist_name):
    url = BASE_URL + 'search'
    search_filter = f'?q={artist_name}&type=artist&limit=1'
    query_url = url + search_filter
    result = requests.get(query_url,headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    result_ = json_result[0]
    result = result_["images"][1]["url"]
    return result

@st.cache_data
def get_artist_name(artist_name):
    url = BASE_URL + 'search'
    search_filter = f'?q={artist_name}&type=artist&limit=1'
    query_url = url + search_filter
    result = requests.get(query_url,headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    result_ = json_result[0]
    result = result_["name"]
    return result    

@st.cache_data
def get_artist_popularity(artist_name):
    url = BASE_URL + 'search'
    search_filter = f'?q={artist_name}&type=artist&limit=1'
    query_url = url + search_filter
    result = requests.get(query_url,headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    result_ = json_result[0]
    result = result_["popularity"]
    return result    

@st.cache_data
def artist_top_tracks(artist_name):
    url  =BASE_URL + f'artists/{get_artist_id(artist_name)}/top-tracks?market=DE'
    result = requests.get(url,headers=headers)
    json_result = json.loads(result.content)['tracks']
    return json_result

@st.cache_data
def get_artist_genre(artist_name):
    url = BASE_URL + 'search'
    search_filter = f'?q={artist_name}&type=artist&limit=1'
    query_url = url + search_filter
    result = requests.get(query_url,headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    result_ = json_result[0]
    result = result_["genres"]
    return result

@st.cache_data
def get_artist_popularity(artist_name):
    url = BASE_URL + 'search'
    search_filter = f'?q={artist_name}&type=artist&limit=1'
    query_url = url + search_filter
    result = requests.get(query_url,headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    result_ = json_result[0]
    result = result_["popularity"]
    return result

    
#artist_id = '36QJpDe2go2KgaRleHCDTp'
#result = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', 
#                 headers=headers, 
#                 )
#data = result.json()
#for album in data['items']:
#    print(album['name'], ' --- ', album['release_date'])
#x = get_artist_id("Drake")
#final_answer = (x["id"])
#result = requests.get(f'https://api.spotify.com/v1/artists/{final_answer}/top-tracks?market=IN',headers=headers)
#print(result)



#songs = (artist_top_tracks("Rajkumar"))
##for song in songs:
##    print(song['url'])
#artist_images = {}
#for item in songs:
#    for artist in item["artists"]:
#        artist_id = artist['id']
#        image_url = item['album']['images'][0]['url']  # Assuming you want the first image URL from the album
#        artist_images[artist_id] = image_url
#    
#for artist_id, image_url in artist_images.items():
#    print(f"Artist ID: {artist_id}, Image URL: {image_url}")
