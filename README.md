# Netflix Shows Recommender System 🎮

This repository contains two main components for building and exploring a Netflix shows recommendation system:

1. **Jupyter Notebook (`.ipynb`)**: A detailed walkthrough of the data exploration, preprocessing, and recommendation model building.
2. **Streamlit App (`app.py`)**: A user-friendly web application to interact with the recommendation system and explore insights such as top genres, cast, countries, and directors.

## Project Overview

This project aims to provide a **Netflix Recommender System** by utilizing **content-based filtering**. The system suggests similar shows based on the user's input and displays interesting insights like top genres, popular cast members, countries with the most movies, and top directors by the number of movies.

The project consists of:

- **Data Preprocessing**: The dataset is cleaned and processed to extract useful features such as genres, cast, countries, and directors.
- **Recommendation Engine**: The model is built using cosine similarity between movie features to recommend shows similar to the ones the user likes.
- **Streamlit Web App**: The app allows users to interact with the recommendation engine and explore various insights.

## Jupyter Notebook

The Jupyter notebook (`notebook.ipynb`) contains the following steps:

1. **Loading the Data**: Import the movie dataset and perform initial exploration.
2. **Data Preprocessing**: Clean the dataset by handling missing values and normalizing features like genres, cast, etc.
3. **Similarity Calculation**: Use vectorized features such as genres and cast to compute similarity scores for the recommendation system.
4. **Model Building**: Implement a content-based recommendation algorithm using cosine similarity.

## Streamlit App

The `app.py` file provides a **web-based interface** for the recommendation system. The app includes the following sections:

- **Recommendations Tab**: Users can select a show and get top 5 similar recommendations.
- **Top Genres Tab**: Displays the top 10 genres by the number of shows.
- **Top Cast Tab**: Displays the top 10 actors and actresses by the number of shows.
- **Top Countries Tab**: Displays the top 10 countries that have the most shows.
- **Top Directors Tab**: Displays the top 10 directors with the most shows.

### Features

- **Movie Recommendations**: Get movie suggestions based on your preferences.
- **Insights**: Explore the most popular genres, cast, countries, and directors.

## Installation

To get started with the project, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/Netflix-show-recommender.git
   cd Netflix-show-recommender
   ```

2. **Install the required packages**:

   Use `pip` or `conda` to install the dependencies.

   ```bash
   pip install -r requirements.txt
   ```

   Or create an environment using `conda`:

   ```bash
   conda create --name recommender-env python=3.8
   conda activate recommender-env
   pip install -r requirements.txt
   ```

   **Requirements:**

   - `streamlit`
   - `pandas`
   - `pickle`
   - `scikit-learn`
   - `numpy`

## Usage

### Running the Streamlit App

To run the Streamlit app locally:

```bash
streamlit run app.py
```

Once the app is running, open a web browser and go to the URL provided (usually `http://localhost:8501`) to start interacting with the recommendation system.

### Running the Jupyter Notebook

1. Open the Jupyter notebook with:

   ```bash
   jupyter notebook notebook.ipynb
   ```

2. Execute the cells to understand the data, preprocessing steps, and how the recommendation system was built.

## Contributing

Feel free to fork this repository, submit issues, and create pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
