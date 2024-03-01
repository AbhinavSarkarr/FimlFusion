import streamlit as st 
import pickle
import pandas as pd
import requests

st.set_page_config(layout="wide")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=29cbc5b90db066f03c77f72d0102738d&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:41]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movieslist = pickle.load(open('/home/jellyfish/Documents/Machine Learning/Recommender System/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movieslist)

similarity = pickle.load(open('/home/jellyfish/Documents/Machine Learning/Recommender System/similairty.pkl', 'rb'))
st.title('Movie Recommender System')

selectedmovie = st.selectbox('Hi',movies['title'].values)

if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(selectedmovie)
    # col1, col2, col3, col4, col5 = st.beta_columns(5)
    #cols = st.columns(10)
    
    # with col1:
    #     st.text(recommended_movie_names[0])
    #     st.image(recommended_movie_posters[0])
    # with col2:
    #     st.text(recommended_movie_names[1])
    #     st.image(recommended_movie_posters[1])
    # with col3:
    #     st.text(recommended_movie_names[2])
    #     st.image(recommended_movie_posters[2])
    # with col4:
    #     st.text(recommended_movie_names[3])
    #     st.image(recommended_movie_posters[3])
    # with col5:
    #     st.text(recommended_movie_names[4])
    #     st.image(recommended_movie_posters[4])


    # cols = st.columns(len(recommended_movie_names))
    # for i in range(len(recommended_movie_names)):
    #         with cols[i]:
    #             st.text(recommended_movie_names[i])
    #             st.image(recommended_movie_posters[i], use_column_width=True)
               

    # # Custom HTML layout for grid with 4 movies per row
    # st.markdown(
    #     """
    #     <style>
    #         .grid-container {
    #             display: grid;
    #             grid-template-columns: repeat(4, 1fr);
    #             grid-gap: 20px;
    #             padding: 10px;
    #             margin: 0 auto;
    #             max-width: 1200px;
    #         }

    #         .grid-item {
    #             display: flex;
    #             flex-direction: column;
    #             align-items: center;
    #             text-align: center;
    #         }

    #         .grid-item img {
    #             max-width: 100%;
    #             height: auto;
    #         }
    #     </style>
    #     """
    # , unsafe_allow_html=True)

    # st.markdown(
    #     """
    #     <div class="grid-container">
    #     """
    # , unsafe_allow_html=True)

    # for movie_name, movie_poster in zip(recommended_movie_names, recommended_movie_posters):
    #     st.markdown(
    #         f"""
    #         <div class="grid-item">
    #             <img src="{movie_poster}" alt="{movie_name}">
    #             <p>{movie_name}</p>
    #         </div>
    #         """
    #     , unsafe_allow_html=True)

    # st.markdown(
    #     """
    #     </div>
    #     """
    # , unsafe_allow_html=True)


        # Custom HTML layout for grid with 4 movies per row
    col1, col2, col3, col4 = st.columns(4)
    
for i in range(len(recommended_movie_names)):
    if i % 4 == 0:
        with col1:
            st.image(recommended_movie_posters[i], use_column_width=True)
            st.markdown(f"<h3 style='font-family: 'Courier New', Courier, monospace; font-size: 20px; color: #333;'>{recommended_movie_names[i]}</h3>", unsafe_allow_html=True)
    elif i % 4 == 1:
        with col2:
            st.image(recommended_movie_posters[i], use_column_width=True)
            st.markdown(f"<h3 style='font-family: 'Courier New', Courier, monospace; font-size: 20px; color: #333;'>{recommended_movie_names[i]}</h3>", unsafe_allow_html=True)
    elif i % 4 == 2:
        with col3:
            st.image(recommended_movie_posters[i], use_column_width=True)
            st.markdown(f"<h3 style='font-family: 'Courier New', Courier, monospace; font-size: 20px; color: #333;'>{recommended_movie_names[i]}</h3>", unsafe_allow_html=True)
    elif i % 4 == 3:
        with col4:
            st.image(recommended_movie_posters[i], use_column_width=True)
            st.markdown(f"<h3 style='font-family: 'Courier New', Courier, monospace; font-size: 20px; color: #333;'>{recommended_movie_names[i]}</h3>", unsafe_allow_html=True)