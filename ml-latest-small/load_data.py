import pandas as pd

# Define file paths for CSV files
links_file_path = "C:\\Users\\saish\\OneDrive\\Desktop\\ML Project\\ml-latest-small\\links.csv"
movies_file_path = "C:\\Users\\saish\\OneDrive\\Desktop\\ML Project\\ml-latest-small\\movies.csv"
ratings_file_path = "C:\\Users\\saish\\OneDrive\\Desktop\\ML Project\\ml-latest-small\\ratings.csv"
tags_file_path = "C:\\Users\\saish\\OneDrive\\Desktop\\ML Project\\ml-latest-small\\tags.csv"

# Read CSV files into DataFrames
links_df = pd.read_csv(links_file_path)
movies_df = pd.read_csv(movies_file_path)
ratings_df = pd.read_csv(ratings_file_path)
tags_df = pd.read_csv(tags_file_path)

# Display the first few rows of each DataFrame to verify the data is loaded correctly
print("Links DataFrame:")
print(links_df.head())

print("\nMovies DataFrame:")
print(movies_df.head())

print("\nRatings DataFrame:")
print(ratings_df.head())

print("\nTags DataFrame:")
print(tags_df.head())
# Compute summary statistics for each DataFrame
links_summary = links_df.describe()
movies_summary = movies_df.describe()
ratings_summary = ratings_df.describe()
tags_summary = tags_df.describe()

# Display the summary statistics
print("Summary Statistics for Links DataFrame:")
print(links_summary)

print("\nSummary Statistics for Movies DataFrame:")
print(movies_summary)

print("\nSummary Statistics for Ratings DataFrame:")
print(ratings_summary)

print("\nSummary Statistics for Tags DataFrame:")
print(tags_summary)

import matplotlib.pyplot as plt

# Histogram of movie ratings (use the "hist()" function to create histogram)
plt.hist(ratings_df['rating'], bins=10, color='skyblue', edgecolor='black')
plt.title(' Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Box plot for movie ratings(use the "boxplot()" function to create a box plot)
plt.figure(figsize=(8, 6))
plt.boxplot(ratings_df['rating'])
plt.title('Box Plot of Movie Ratings')
plt.xlabel('Movies')
plt.ylabel('Ratings')
plt.grid(True)
plt.show()

# Scatter plot of movie ratings vs. Movies (use the "scatter()" function to create a scatter plot)

plt.figure(figsize=(8, 6))
plt.scatter(ratings_df['movieId'], ratings_df['rating'], alpha=0.5)
plt.title('Scatter Plot of Movie Ratings vs. Timestamps')
plt.xlabel('Movies')
plt.ylabel('Ratings')
plt.grid(True)
plt.show()
