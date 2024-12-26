import streamlit as st
import pickle
import pandas as pd

shows = pd.DataFrame(pickle.load(open('shows.pkl', 'rb')))
show_mod = pickle.load(open('shows_modified.pkl', 'rb'))
shows_mod = pd.DataFrame(show_mod)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(show):
    show_index = shows_mod[shows_mod['title'] == show].index[0]
    distances = similarity[show_index]
    show_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_show = []
    for i in show_list:
        recommended_show.append(shows.iloc[i[0]].title)

    return recommended_show

st.title('🎬 Netflix Recommender System 🍿')

# Create a sidebar with options for different tabs
tabs = ["🎥 Recommendations", "🌟 Top Genres", "🎭 Top Cast", "🌍 Top Countries", "🎬 Top Directors"]
selected_tab = st.sidebar.radio("Select a tab", tabs)

if selected_tab == "🎥 Recommendations":
    st.subheader("🤔 Movie Recommendations based on your preference:")
    selected_show_name = st.selectbox("Which movie do you like?", shows_mod['title'].values)
    
    if st.button('🔍 Recommend'):
        recommendations = recommend(selected_show_name)
        st.write(f"Here are the top 5 recommendations based on {selected_show_name}:")
        for i, recommendation in enumerate(recommendations, 1):
            st.write(f"{i}. {recommendation} 🎬")

elif selected_tab == "🌟 Top Genres":
    st.subheader("🌟 Top 10 Genres by Number of Movies")
    top_genres = shows['genre'].explode().value_counts().head(10)
    st.write(top_genres)

elif selected_tab == "🎭 Top Cast":
    st.subheader("🎭 Top 10 Cast by Number of Movies")
    top_cast = shows['cast'].explode().value_counts()[1:11]
    st.write(top_cast)

elif selected_tab == "🌍 Top Countries":
    st.subheader("🌍 Top 10 Countries by Number of Movies")
    top_countries = shows['country'].value_counts().head(10)
    st.write(top_countries)

elif selected_tab == "🎬 Top Directors":
    st.subheader("🎬 Top 10 Directors by Number of Movies")
    top_directors = shows['director'].value_counts()[1:11]
    st.write(top_directors)