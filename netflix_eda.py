import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset
df = pd.read_csv("netflix_titles.csv")

#shape
df.shape

#columns
df.columns

#missing values
df.isnull().sum()

#remove duplicates
df.drop_duplicates(inplace=True)
df.duplicated().sum()

#convert date column
df.info()
df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(
    df['date_added'],
    errors='coerce'
)
df.info()

#null values
df.isnull().sum()
df['country'].fillna('Unknown', inplace=True)
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Not Available', inplace=True)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)
df.dropna(subset=['duration'], inplace=True)
df.dropna(subset=['date_added'], inplace=True)
df.isnull().sum()

#save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)


#1.Movies vs TV shows
df['type'].value_counts().plot(kind='bar')
plt.title('Movies vs TV Show on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.savefig('movies_vs_tv_shows.png')
plt.show()
# Observation:
# Movies significantly outnumber TV Shows on Netflix.
# This indicates that Netflix's content library is primarily movie-focused.


#2.Content added each year
df['year_added'] = df['date_added'].dt.year

content_year = df['year_added'].value_counts().sort_index()
content_year

content_year.plot(kind='line')
plt.title('Content Added Each Year on Netflix')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.xticks(rotation=0)
plt.savefig('content_added_each_year.png')
plt.show()
# Observation:
# The number of titles added to Netflix increased rapidly after 2015.
# Netflix experienced its fastest content expansion between 2018 and 2020.


#3.Top 10 countries producing content
top_countries = df['country'].value_counts().head(10)
top_countries

top_countries.plot(kind='bar')
plt.title('Top 10 Countries Producing Content on Netflix')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.savefig('top_10_countries.png')
plt.show()
# Observation:
# The United States contributes the highest number of titles on Netflix.
# India is also among the leading content-producing countries.
# Netflix hosts content from a diverse range of countries worldwide.


#4.Most common rating
df['rating'].value_counts()

df['rating'].value_counts().plot(kind='bar')
plt.title('Most Common Ratings on Netflix')
plt.xlabel('Rating')
plt.ylabel('Number of Titles')
plt.xticks(rotation=90)
plt.savefig('most_common_ratings.png')
plt.show()
# Observation:
# TV-MA is the most common rating on Netflix.
# This suggests that a large portion of Netflix content is targeted toward mature audiences.


#5.Most common genres
df['listed_in'].value_counts().head(10)

df['listed_in'].value_counts().head(10).plot(kind='bar')
plt.title('Most Common Genres on Netflix')
plt.xlabel('Genre')
plt.ylabel('Number of Titles')
plt.xticks(rotation=90)
plt.savefig('most_common_genres.png') 
plt.show()
# Observation:
# Drama and International content are among the most common genres on Netflix.
# This highlights Netflix's focus on diverse and globally appealing content.


#6.Which release years dominate
release_years = df['release_year'].value_counts().sort_index()
release_years

release_years.plot(kind='line')
plt.title('Release Years of Netflix Titles')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.xticks(rotation=0)
plt.savefig('release_years.png')
plt.show()
# Observation:
# Most Netflix titles were released in recent years.
# Older titles are present but form a smaller portion of the catalogue.


#7.Top 10 Directors
top_directors = (
    df[df['director'] != 'Unknown']['director']
    .value_counts()
    .head(10)
)
top_directors

top_directors.plot(kind='bar')
plt.title('Top 10 Directors on Netflix')
plt.xlabel('Director')
plt.ylabel('Number of Titles')
plt.xticks(rotation=90)
plt.savefig('top_directors.png')
plt.show()
# Observation:
# A small group of directors contributes multiple titles to Netflix.
# Certain directors have a stronger presence on the platform compared to others.
# Rajiv Chilaka appears as one of the most frequent directors on Netflix.
# This indicates a strong presence of animated and children's content.


#8.Movie duration distribution
movies = df[df['type'] == 'Movie'].copy()
movies['duration_time'] = movies['duration'].str.replace(' min', '').astype(int)

movies['duration_time'].hist(bins=20)
plt.title('Movie Duration Distribution on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.savefig('movie_duration_distribution.png')
plt.show()
# Observation:
# Most movies on Netflix have durations between 80 and 120 minutes.
# Extremely short and extremely long movies are relatively uncommon.




#Additional Visualization

#Movies vs TV shows : Pie chart
df['type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Movies vs TV Show on Netflix')
plt.ylabel('')
plt.savefig('movies_vs_tv_shows_pie.png')
plt.show()
# Observation:
# Movies make up the majority of Netflix's catalogue.
# TV Shows account for a smaller but significant share of available content.


#Correlation between release year and year added: Heatmap
numeric_df = df[['release_year', 'year_added']]
numeric_df

sns.heatmap(numeric_df.corr(), annot=True)
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()
# Observation:
# The correlation between release year and year added is positive.
# Newer titles tend to be added to Netflix more frequently than older titles.




print("Key Insights from Netflix EDA:")
print("1. Movies dominate Netflix's content library.")
print("2. Netflix expanded aggressively after 2015.")
print("3. The United States is the largest content contributor.")
print("4. TV-MA is the most common rating.")
print("5. Drama and International genres are highly represented.")
print("6. Most movies are between 80 and 120 minutes long.")
print("7. Newer titles are added to Netflix more frequently than older titles.")

