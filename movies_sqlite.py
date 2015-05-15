with sqlite3.connect('movies_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Movies")
    c.execute("CREATE TABLE People(imdbID TEXT, Title TEXT, imdbRating INT...)")
    for i in range(0, len(name of your movie list):
        c.execute("INSERT INTO Movies VALUES(?, ?, )")
    
    
