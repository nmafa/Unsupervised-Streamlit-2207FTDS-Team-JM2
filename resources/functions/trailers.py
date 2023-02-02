import urllib.request
import requests
import unicodedata
import re
from streamlit_player import st_player

def trailers(top_10):
    search = unicodedata.normalize('NFKD', top_10).encode('ascii', 'ignore').decode()
    youtube_search = re.sub("[ ]", "+", search)
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + youtube_search + '+trailer')
    vid_id = re.findall(r'watch\?v=(\S{11})', html.read().decode())
    
    movie_trail = 'https://www.youtube.com/watch?v=' + vid_id[0]
    st_player( movie_trail)