import sqlite3
import requests
conn = sqlite3.connect('movies.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY,title TEXT,release_date TEXT,cast TEXT
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS reviews(id INTEGER PRIMARY KEY,movie_id INTEGER,review TEXT
)''')
conn.commit()
api_key = "c2724de1"
movie_name = input("enter movie name:")
url = f"https://www.omdbapi.com/?apikey={api_key}&t={movie_name}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data.get("Response") == "True":
        title = data.get("Title")
        year = data.get("Year")
        cast = data.get("Actors")
        plot = data.get("Plot")


        cursor.execute("INSERT INTO movies (title, release_date, cast) VALUES (?, ?, ?)",(title,year,cast))
        conn.commit()
        movie_id = cursor.lastrowid

        print("TITLE:", title)
        print("YEAR:" ,year)
        print("CAST:", cast)
        print("PLOT:", plot)

        review = input("enter your review for this movie:")
        cursor.execute("INSERT INTO reviews(movie_id, review) VALUES(?,?)",(movie_id,review))

        conn.commit()
        print("Review Saved!")
    else:
        print("Movie not found")
else:
 print("failed to get movie from  api")

conn.close()
      



