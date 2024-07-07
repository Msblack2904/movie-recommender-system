import pickle
import streamlit as st
import requests




def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


html_temp = """ 
    <div style ="
  border: 2px solid black;
  padding: 2px;
  background-color : tomato;
  background-size: 600px 200px;"> 
    <h4 style ="color:black;text-align:center;">Movie Recommender System</h4> 
    </div> 
    """

# this line allows us to display the front end aspects we have
# defined in the above code
st.markdown(html_temp, unsafe_allow_html=True)
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Select your favorite movie from the dropdown',
    movie_list
)

if st.button('Show Recommendation'):
    html_temp = """ 
        <div style ="
      border: 2px solid black;
      padding: 0px;
      background-color : LightGray;
      background-size: auto;"> 
        <h5 style ="color:black;text-align:center;padding-top: 10px;
  padding-right: 30px;
  padding-bottom: 10px;
  padding-left: 30px;">You can also watch</h5> 
        </div> 
        """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    recommended_movie_names= recommend(selected_movie)
    st.subheader(recommended_movie_names[0])
    st.subheader(recommended_movie_names[1])
    st.subheader(recommended_movie_names[2])
    st.subheader(recommended_movie_names[3])
    st.subheader(recommended_movie_names[4])
    st.subheader(recommended_movie_names[5])
    st.subheader(recommended_movie_names[6])
    st.subheader(recommended_movie_names[7])
    st.subheader(recommended_movie_names[8])
    st.subheader(recommended_movie_names[9])

