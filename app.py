import streamlit as st
import pickle
import pandas as pd
import requests

import gzip
import pickle






# Fetch movie posters from the TMDB API
def fetch_posters(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=f2a9ed339841fbb8668837ba44676377&language=en-US'
    )
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"

# Fetch movie trailer from the TMDB API
def fetch_trailer(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=f2a9ed339841fbb8668837ba44676377&language=en-US'
    )
    data = response.json()
    if data['results']:
        trailer_key = data['results'][0]['key']  # Get the first trailer
        return f"https://www.youtube.com/watch?v={trailer_key}"
    return None

# Fetch top-rated movies from TMDB API
def fetch_top_rated_movies():
    api_key = '763e6acc6b64aca60d259d7de6a5dc04'  # Your API Key
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url)
    data = response.json()
    return data['results']

# Fetch trending movies from TMDB API
def fetch_trending_movies():
    api_key = '763e6acc6b64aca60d259d7de6a5dc04'  # Your API Key
    url = f'https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['results']

# Load movie data and similarity model
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Open the compressed file with gzip
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# Title and description
st.title('🎬 Movie Recommender')
st.markdown("<h3 style='font-size:24px;'>Find movies you'll love based on your favorite selections!</h3>", unsafe_allow_html=True)

# Dropdown search bar for movie selection
selected_movie_name = st.selectbox('Search and select a movie:', options=[''] + list(movies['title'].values))

# Sidebar for filters
st.sidebar.header("Customize Your Recommendations")
st.sidebar.selectbox('Genre Preference', ['All', 'Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi'])
st.sidebar.slider('Release Year', min_value=1980, max_value=2023, value=(2000, 2023))

# Recommendation logic]

def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []
        movie_name_base = movie.split(' ')[0].lower()  # Get the base name for comparison
        
        for i in movies_list:
            # Filter out the same franchise
            if movie_name_base not in movies.iloc[i[0]].title.lower():
                movie_id = movies.iloc[i[0]].movie_id
                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_posters(movie_id))
        
        return recommended_movies, recommended_movies_posters
    except IndexError:
        return [], []  
   


if st.button('Recommend'):
    if selected_movie_name in movies['title'].values:
        names, posters = recommend(selected_movie_name)
        if names:
            cols = st.columns(5)
            for i, col in enumerate(cols):
                if i < len(names):
                    with col:
                        st.image(posters[i], caption=names[i], use_container_width=True)
        else:
            st.warning("No recommendations found. Try selecting a different movie.")
    else:
        st.error("Movie not found! Please check your input or select another movie.")

# Display top-rated or trending movies
def display_movies(movie_list):
    cols = st.columns(5)
    for i, movie in enumerate(movie_list):
        if i % 5 == 0 and i > 0:
            cols = st.columns(5)
        with cols[i % 5]:
            poster_url = fetch_posters(movie['id'])
            trailer_link = fetch_trailer(movie['id'])
            st.image(poster_url, use_container_width=True)
            st.write(f"**{movie['title']}**")
            if trailer_link:
                st.markdown(f"[Watch Trailer](%s)" % trailer_link)



st.subheader("🌟 Explore the Top-Rated Movies")
st.markdown("Discover critically acclaimed movies that are loved by audiences worldwide. Here's a list of the top-rated movies to add to your watchlist!")
top_rated_movies = fetch_top_rated_movies()
display_movies(top_rated_movies)
display_movies(top_rated_movies)

st.subheader("🔥 Trending Movies This Week")
st.markdown("Catch up with the movies everyone is talking about! Here are the trending hits making waves this week.")
trending_movies = fetch_trending_movies()
display_movies(trending_movies)
display_movies(trending_movies)

st.markdown(
    """
    <hr>
    <p style="text-align:center; color:grey;">
        Built using Streamlit by Charu Rajput | <a href="https://github.com/charuu2" target="_blank">GitHub</a>
    </p>
    """,
    unsafe_allow_html=True
)
