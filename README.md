# Movie Recommender 🎬

A user-friendly and interactive movie recommendation system built using **Streamlit** and **TMDB API**. This app helps users discover movies they'll love based on their favorite selections and also explore top-rated and trending movies.

---

## Features ✨

- **Personalized Recommendations**: Get 5 movie recommendations based on the movie you select.
- **Movie Posters**: Displays posters of recommended movies fetched via TMDB API.
- **Top-Rated Movies**: Discover critically acclaimed movies loved by audiences worldwide.
- **Trending Movies**: Catch up on the movies making waves this week.
- **Watch Trailers**: Links to trailers for top-rated and trending movies.
- **Filters**: Customize recommendations with genre preferences and release year range.

---

## How It Works 🛠️

1. **Select a Movie**: Use the dropdown search bar to select your favorite movie.
2. **Hit Recommend**: Get personalized recommendations along with posters.
3. **Explore Movies**: Browse through the top-rated and trending movies.

---

## Installation 🧰

1. Clone the repository:
   ```bash
   [git clone https://github.com/charuu2/moviesystem.git](https://github.com/priyalakshmi24/Movie-recommendation-system.git)
   ```

2. Navigate to the project directory:
   ```bash
   cd moviesystem
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser at `http://localhost:8501`.

---

## TMDB API Configuration 🔑

1. Sign up for a TMDB account at <a href="https://www.themoviedb.org/?language=en-US" target="_blank">tmdb</a>
2. Go to your API settings and generate an API key.
3. Replace the placeholders in the code with your TMDB API key:
   ```python
   api_key = 'YOUR_TMDB_API_KEY'
   ```

---

## File Details 📂

- `app.py`: The main application file containing the Streamlit code.
- `movie_dict.pkl`: Pre-processed movie data dictionary.
- `similarity.pkl`: Similarity matrix for movie recommendations.
- `requirements.txt`: Python dependencies for the project.

---

## Screenshots 📸

- **Recommendation Page**:
   <img width="1470" alt="Image" src="https://github.com/user-attachments/assets/c3ba7371-a7f1-46bb-8086-51758b3d89e7" />

    <img width="1470" alt="Image" src="https://github.com/user-attachments/assets/55a09bd1-1896-4138-b532-4fe38331ce27" />

    <img width="1470" alt="Image" src="https://github.com/user-attachments/assets/90ede612-782b-47dc-be0d-65237080c04d" />
 

- **Top-Rated Movies Section**:
<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/565e4ce6-6050-4fd0-877e-aee9c47a32f5" />

- **Trending Movies Section**:
  <img width="1470" alt="Image" src="https://github.com/user-attachments/assets/db80cd6b-594c-471d-aeeb-488af9e60a99" />

---

## Built With 🛠️

- **Python**: Programming language for building the app.
- **Streamlit**: Framework for creating the interactive web app.
- **TMDB API**: Fetching movie data, posters, and trailers.
- **Pandas**: Data manipulation and analysis.

---

## Problem Statement :

In today’s digital entertainment landscape, users are bombarded with a wide variety of movies, making it challenging to discover films that match their preferences. A movie recommendation system can help users navigate this vast collection by predicting and suggesting movies they are likely to enjoy based on their historical behavior, preferences, and the behavior of other users with similar tastes.

## Concepts

- **Data Analysis**: Explore and preprocess movie data from TMDb.
- **Recommendation Algorithms**: Implement various algorithms to generate movie recommendations.
- **Content-Based Filtering**: Recommends movies similar to those a user has liked based on movie attributes.
- **Collaborative Filtering**: Suggests movies based on the preferences of similar users.
- **Hybrid Approach**: Combines multiple recommendation techniques for improved accuracy.

## Dataset

The dataset used in this project is sourced from TMDb and includes the following features:
- `movie_id`: Unique identifier for each movie.
- `title`: Title of the movie.
- `overview`: Brief description of the movie.
- `release_date`: Release date of the movie.
- `genres`: Genres associated with the movie.
- `vote_average`: Average rating of the movie.
- `vote_count`: Number of votes the movie has received.
- `popularity`: Popularity score of the movie.
- `cast`: Main cast members of the movie.
- `crew`: Key crew members of the movie.

---

## Steps for Data Preparation and Analysis

1. **Data Cleaning**
   - **Removed Missing Values**: Identified and removed missing values in key columns, such as movie titles, genres, and other critical attributes. This step was essential to ensure that the analysis and models would not be negatively impacted by incomplete data.
   - **Handled Incomplete Entries**: Addressed any incomplete entries by either filling in gaps with appropriate default values or removing those records, ensuring a consistent and reliable dataset.

2. **Data Transformation**
   - **Feature Engineering**: 
     - Created new features by combining multiple columns. This included extracting relevant information such as genres, keywords, cast, and crew to form more informative features that could enhance the recommendation process.
   - **Lowercasing**: Converted all text data to lowercase to maintain consistency and avoid issues related to case sensitivity. This transformation helps ensure that text comparisons are accurate and reliable.

3. **Feature Extraction**
   - **Genres, Keywords, Cast, and Crew**: Relevant information was extracted from the original dataset to create structured data. This involved isolating key features that would later be used in the recommendation algorithm. 
   - **Tag Creation**: Combined the movie overview, cast, crew, genres, and keywords into a single text string called ‘tags’. This single string format simplifies the process of similarity calculations and model training by providing a comprehensive representation of each movie.

4. **Data Structuring**
   - **Merging Data**: Merged the movies and credits datasets into one cohesive dataset. This step involved combining information about the movies (e.g., titles, release dates, genres) with information about the cast and crew (e.g., actors, directors). The merged dataset provides a unified view that is easier to analyze and work with.

5. **Cosine Similarity Calculation**
   - **Measuring Similarity**: Calculated cosine similarity to measure the similarity between movies based on their tags. This mathematical metric helps determine how alike two movies are based on their combined features, which is crucial for making personalized recommendations.

6. **Data Visualization**
   - **Histograms and Bar Charts**: Plotted various visualizations, including histograms and bar charts, to showcase the distribution of movie ratings and other relevant metrics. This included visualizing the distribution of ratings to understand user preferences better and identifying trends.
   - **Top 10 Movie Keywords**: Created bar charts to display the top 10 movie keywords, allowing for a quick overview of the most common themes and subjects present in the dataset.

---

## Expected Outcome:
A machine learning-based movie recommendation system that continuously learns and improves based on user interactions, delivering personalized movie suggestions and enhancing the overall user experience.

---

## Acknowledgements 🙌

- Special thanks to [TMDB](https://www.themoviedb.org/) for their amazing API.
- Powered by **Streamlit** for effortless web app development.

---

## About the Developer 👩‍💻

Built with ❤️ by **Priyalakshmi Agarwal**



Feel free to ⭐ the repository if you found it useful!

---

This version includes the updated repo name (`moviesystem`) and fixes any minor discrepancies!
